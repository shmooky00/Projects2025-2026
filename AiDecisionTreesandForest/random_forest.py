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
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import sys
import math


test_pct = 0.2
n_estimators = 100
max_depth = None

if len(sys.argv) == 1:
    print(f'Usage: python random_forest.py train tpct max_depth [n_estimators]')
    print('Where:') 
    print('   train - will train and then test the model')
    print('   tpct is the percent of data to use for testing - value is')
    print('        between 0.0 and 1.0.  If not provided, will default to 0.2.')
    print('   max_depth is the maximum depth of the trees (use None for unlimited)')
    print('   n_estimators is optional, number of trees in forest (default: 100)')
    sys.exit()

#
#   Process command line arguments
#
if sys.argv[1] == 'train':
    run_type = 'train'
    if len(sys.argv) >= 3 and float(sys.argv[2]) > 0.0 and float(sys.argv[2]) < 1.0:
        test_pct = float(sys.argv[2])
    if len(sys.argv) >= 4:
        if sys.argv[3].lower() == 'none':
            max_depth = None
        else:
            max_depth = int(sys.argv[3])
    if len(sys.argv) >= 5:
        n_estimators = int(sys.argv[4])
else:
    print('Invalid option chosen. Valid value is train')
    sys.exit()

#
#   Open the input data file and read in the data
#
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


# Tip - You may want to discretize the age parameter to use ranges and not absolute values

df = pandas.DataFrame(a)
num_rows = df.shape[0]
num_test = math.floor(num_rows * test_pct)
num_train = num_rows - num_test

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

feature_names = [col for col in df.columns if col not in ['id', 'purchased']]


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


# TODO Create the random forest classifier using scikit-learn. Directions are in Activity 10
# in the textbook.  

#i couldnt find activity 10 but i used this reference to help https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
random_forest = RandomForestClassifier(
    n_estimators=n_estimators,
    max_depth=max_depth,
    criterion='entropy',
    random_state=42,
    n_jobs=-1
)
#end of reference

print(f'\nTraining Random Forest with {n_estimators} trees, max_depth={max_depth}')
random_forest = random_forest.fit(features_train, label_train)

# TODO Implement the feature_importances function and report on which features are of greatest and least importance.

print('\nFeature Importance Analysis:')
feature_importance = pandas.Series(random_forest.feature_importances_, index=feature_names).sort_values(ascending=False)

print('\nFeature Importance Rankings:')
for idx, (feature, importance) in enumerate(feature_importance.items(), 1):
    print(f'  {idx}. {feature}: {importance:.4f}')

print(f'\nMost important feature: {feature_importance.index[0]} ({feature_importance.iloc[0]:.4f})')
print(f'Least important feature: {feature_importance.index[-1]} ({feature_importance.iloc[-1]:.4f})')

#took inspo from the feature importance and visualization section of https://github.com/Challameghana06/Descision-Tree/blob/main/Decision%20Tree.ipynb
plt.figure(figsize=(10, 5))
feature_importance.plot(kind='bar')
plt.title('Feature Importance - Random Forest')
plt.xlabel('Features')
plt.ylabel('Importance')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('feature_importance.png') #made it save the graphs because showing it made some type of error loop
plt.close()
print(f'\nFeature visulaization saved to feature_importance.png')
#end of reference

if test_pct > 0.025:
    y_predict = random_forest.predict(features_test)
    print(f'\nScore: {random_forest.score(features_test, label_test):.4f}')
    print('\nClassification Report:')
    print(
        classification_report(
            label_test,
            y_predict,
            zero_division=0         
        )
    )  


# TODO For our report, vary the parameters of RandomForestClassifier to see how they impact the output. 
# You will include these findings in your report.