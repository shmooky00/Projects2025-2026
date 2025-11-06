'''

In-class demo code to create a decision tree.  You may use what you learn here as
part of the course project.

Input data file comes from here: https://archive.ics.uci.edu/dataset/19/car+evaluation

'''
import pandas
import numpy as np
from sklearn import preprocessing
from sklearn import tree
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# For graphing final tree
import graphviz

# For handling command line arguments
import sys
import math

# Default Values
test_pct = 0.2
m_depth = 6

#
#   Process command line input
#
if len(sys.argv) == 1:
    print(f'Usage: python cars.py type tpct depth')
    print('Where:') 
    print('   type is either train - will train and then test the model or,')
    print('        all - will use all but one data sample to build the model')
    print('   tpct is used in train mode to specify percent of data to use for testing - value is')
    print('        between 0.0 and 1.0.  If not provided, will default to 0.2.')
    print('   depth is used to set the depth (number of levels) in the resulting tree')
    sys.exit()

if sys.argv[1] == 'train':
    # do training run and test for stats
    run_type = 'train'

    # Set test percentage
    if len(sys.argv) == 3 and float(sys.argv[2]) > 0.0 and float(sys.argv[2]) < 1.0:
        test_pct = float(sys.argv[2])

elif sys.argv[1] == 'all':
    run_type = 'all'
    test_pct = 0.0

else:
    print('Invalid option chosen. Valid values are train and all')
    sys.exit()


if run_type == 'train' and len(sys.argv) == 4:
    # Set max Depth
    m_depth = int(sys.argv[3])
elif run_type == 'all' and len(sys.argv) == 3:
    # Set max Depth
    m_depth = int(sys.argv[2])

#
#   END of Input processing
#




# Read data from file and get number of rows
df = pandas.read_csv('./data/car_eval.csv')
num_rows = df.shape[0]

# Set the amount of testing and training data
if run_type == 'all':
    num_train = num_rows - 1
    num_test = 1    # sklearn requires at least one row of testing data
else:
    # Calculate number of test and training rows from user input
    num_test = math.floor(num_rows * test_pct)
    num_train = num_rows - num_test


# Names of the freatures for graphviz output
feature_names = ['Buying', 'Maint', 'Doors', 'Persons', 'LuggageBoot', 'Safety']

# Discretized names for each label
labels = {
    'Buying': ['low','med', 'high', 'vhigh'],
    'Maint': ['low','med', 'high', 'vhigh'],
    'Doors': ['2', '3', '4', '5more'],
    'Persons': ['2', '4', 'more'],
    'LuggageBoot': ['small', 'med', 'big'],
    'Safety': ['low', 'med', 'high'],
    'Class': ['unacc', 'acc', 'good', 'vgood']
}

#
#   Create dataframe to process file data
#
label_encoders = {}
df_encoded = pandas.DataFrame()
for column in df:
    if column in labels:
        # Encode labels from text to numeric values
        label_encoders[column] = preprocessing.LabelEncoder()
        label_encoders[column].fit(labels[column])

        # Build df of encoded data
        df_encoded[column] = label_encoders[column].transform(df[column])
    else:
        df_encoded[column] = df[column]

# Extract features from the encoded dataframe
features = np.array(df_encoded.drop(['Class'], axis=1))

# Extract the labels from the encoded dataframe
label = np.array(df_encoded['Class'])

# Generate Training and Testing Data
features_train, features_test, label_train, label_test = model_selection.train_test_split(
    features,
    label,
    train_size = num_train,
    test_size = num_test
)

# Create the Decision Tree based on the training data
decision_tree = DecisionTreeClassifier(criterion='entropy',
                                       max_depth=m_depth,
                                       min_samples_leaf=1)

decision_tree = decision_tree.fit(features_train, label_train)


# Plot your tree to a pdf file
dot_data = tree.export_graphviz(decision_tree, out_file=None,
                                feature_names=feature_names,
                                filled=True, rounded=True,
                                special_characters=True) 

graph = graphviz.Source(dot_data) 
graph.render("cars") 


# If training and testing is desired, print the results
if test_pct > 0.025:

    print('Score: ', decision_tree.score(features_test, label_test))
    print('\n\n')
    print(
        classification_report(
            label_test,
            decision_tree.predict(features_test),
            zero_division=0         
        )
    )
