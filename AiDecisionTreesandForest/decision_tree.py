'''
Implement code to calculate the entropy of a dataset and then identify the root node of
a decision tree using the Information Gain method.

Input - car_purchased.csv file that contains attributes of people that bought or didn't
    buy a car.

    Starter code will read the file data into a list of dictionaries where each dictionary 
    entry contains data for one customer interaction in the data file.

Outputs:

    1. Identify the overall entropy of the dataset

    2. Identify the information gain of each attribute in the file

    3. Identify the root node of the decision tree based on item #2.

Potential limitations:

    1. None known at this time

Your code:
    1. 
'''

import csv
import pandas
import numpy as np
from sklearn import preprocessing
from sklearn import tree
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import graphviz
import sys
import math


test_pct = 0.2
m_depth = 6

if len(sys.argv) == 1:
    print(f'Usage: python decision_tree.py type tpct depth')
    print('Where:') 
    print('   type is either train - will train and then test the model or,')
    print('        all - will use all but one data sample to build the model')
    print('   tpct is used in train mode to specify percent of data to use for testing - value is')
    print('        between 0.0 and 1.0.  If not provided, will default to 0.2.')
    print('   depth is used to set the depth (number of levels) in the resulting tree')
    sys.exit()

#
#   Open the input data file and read in the data
#

if sys.argv[1] == 'train':
    # do training run and test for stats
    run_type = 'train'
    if len(sys.argv) >= 3 and float(sys.argv[2]) > 0.0 and float(sys.argv[2]) < 1.0:
        test_pct = float(sys.argv[2])
elif sys.argv[1] == 'all':
    run_type = 'all'
    test_pct = 0.0
else:
    print('Invalid option chosen. Valid values are train and all')
    sys.exit()

if run_type == 'train' and len(sys.argv) == 4:
    m_depth = int(sys.argv[3])
elif run_type == 'all' and len(sys.argv) == 3:
    m_depth = int(sys.argv[2])

with open('./data/car_purchased.csv', newline='', encoding='utf-8-sig') as f:
    a = [{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]
    
# This is provided for you to see what the data looks like
# for r in a:
#   print(r)


#
# Get the keys for each dictionary entry as a list - You may find this helpful
#
keys = list(a[0].keys())
print(keys)

#
# TODO Create a method that accepts input parameters and calculates entropy
#

# used a comment on the thread for help and edited it to fit pandas https://stackoverflow.com/questions/15450192/fastest-way-to-compute-entropy-in-python
def calculate_entropy(data):
    n_labels = len(data)
    if n_labels <= 1:
        return 0
    value_counts = pandas.Series(data).value_counts()
    probs = value_counts / n_labels
    n_classes = len(probs)
    if n_classes <= 1:
        return 0
    ent = 0.0
    for p in probs:
        if p > 0:
            ent -= p * math.log2(p)
    return ent
#end of reference

#
# Pre-process the data and update the dictionaries appropriately
#
df = pandas.DataFrame(a)
num_rows = df.shape[0]

if run_type == 'all':
    num_train = num_rows - 1
    num_test = 1
else:
    num_test = math.floor(num_rows * test_pct)
    num_train = num_rows - num_test


# Tip - You may want to discretize the age parameter to use ranges and not absolute values

df['age'] = pandas.to_numeric(df['age'])
df['age'] = pandas.cut(df['age'], 
                       bins=[0, 25, 35, 50, 100], 
                       labels=['0-25', '26-35', '36-50', '51+'])

# Tip - You may want to discretize the salary paramter to use ranges and not absolute values

df['salary'] = pandas.to_numeric(df['salary'])
df['salary'] = pandas.cut(df['salary'],
                                bins=[0, 30000, 60000, 90000, float('inf')],
                                labels=['Low', 'Medium', 'High', 'VeryHigh'])

overall_entropy = calculate_entropy(df['purchased'])
print(f'Overall entropy of the dataset: {overall_entropy:.4f}')



#used the building tree function section for inspiration on the information gain https://www.geeksforgeeks.org/machine-learning/iterative-dichotomiser-3-id3-algorithm-from-scratch/
print('\nInformation Gain for each attribute:')
info_gains = {}
for attr in ['gender', 'age', 'salary']:
    if attr in df.columns:
        weighted_entropy = 0
        for value in df[attr].unique():
            subset = df[df[attr] == value]['purchased']
            weight = len(subset) / len(df)
            entropy = calculate_entropy(subset)
            weighted_entropy += weight * entropy
        info_gain = overall_entropy - weighted_entropy
        info_gains[attr] = info_gain
        print(f'  {attr}: {info_gain:.4f}')

if info_gains:
    root_node = max(info_gains, key=info_gains.get)
    print(f'\nRoot node: {root_node} ({info_gains[root_node]:.4f})')

#end of inspiration

feature_names = [col for col in df.columns if col not in ['id', 'purchased']]



# TODO Create the decision tree using scikit-learn.  You can use the cars.py code as a template to 
# help you write this code.

label_encoders = {}
df_encoded = pandas.DataFrame()

df_encoded['id'] = df['id']

for column in df.columns:
    if column in ['gender', 'age', 'salary']:
        label_encoders[column] = preprocessing.LabelEncoder()
        df_encoded[column] = label_encoders[column].fit_transform(df[column].astype(str))
    elif column == 'purchased':
        df_encoded[column] = df[column]
    elif column != 'id':
        df_encoded[column] = df[column]

features = np.array(df_encoded.drop(['id', 'purchased'], axis=1))
label = np.array(df_encoded['purchased'])

features_train, features_test, label_train, label_test = model_selection.train_test_split(
    features,
    label,
    train_size=num_train,
    test_size=num_test,
    random_state=42
)

decision_tree = DecisionTreeClassifier(criterion='entropy',
                                       max_depth=m_depth,
                                       min_samples_leaf=1)

decision_tree = decision_tree.fit(features_train, label_train)

if run_type == 'all':
    dot_data = tree.export_graphviz(decision_tree, out_file=None,
                                    feature_names=feature_names,
                                    filled=True, rounded=True,
                                    special_characters=True) 
    graph = graphviz.Source(dot_data) 
    graph.render("decision_tree") 
    print(f'\nDecision tree visualization saved to decision_tree.pdf')

if test_pct > 0.025:
    print(f'\nScore: {decision_tree.score(features_test, label_test):.4f}')
    print('\nClassification Report:')
    print(
        classification_report(
            label_test,
            decision_tree.predict(features_test),
            zero_division=0         
        )
    )  


# TODO For our report, vary the test sample percentage and vary the number of features you include 
# in the model to see how accuracy, precision and recall are affected.  You will include these
# findings in your report.

# also read this to try and get a better understanding of how these work in python, didnt use code though https://www.datacamp.com/tutorial/decision-tree-classification-python

