# Decision Trees
This project will build a decision tree utilizing a dataset from Kaggle.

## Overview
Imagine that you are working at a car dealership and want to identify attributes that more consistently lead to a vehicle purchase decision. Because you just completed an AI course and talked about the merits of decision trees, you feel this may be a worthwhile approach to build your model. You will use the car_data.csv file included here in the starter code to build a decision tree that analyzes purchasing decisions based on historical data.  If you are interested, the data was taken from Kaggle - https://www.kaggle.com/datasets/gabrielsantello/cars-purchase-decision-dataset.

You will write code to do three related things.

1. Use scikit-learn to construct a full decision tree.

2. Use scikit-learn to construct a random forest of decision trees.

You will write a report to discuss your findings.


## The Code
You are being provided starter code for the project. The important/graded ones are:

- **decision_tree.py** - This file provides skeleton code that will read the test data into a pandas dataframe.  From there you can build the decision tree code using scikit-learn. Once the code is working, you will collect data (score, precision, recall, f1) for various depths and percentages of testing data. This information will be used in your report. This program is **40%** of the grade

- **random_forest.py** - This file will be your implementation of the random forest. You should plan on re-using parts of the decision tree code as much as possible. Here you will collect the same kind of data for varying number of estimators and tree depth.  You will also report on the feature_importances to show which features of the model provide the biggest impact to the results.  This information will be used in your report. This program is **40%** of the grade.

To run your code for testing purposes you will do this:
```
python decision_tree.py <train | all> <train_pct if applicable> <max_depth>
python random_forest.py train <train_pct> <max_depth>
```
## The Report
You will also submit a report (worth **20%** of the grade.) The report will be no more than three pages and will address the following:

1. Analysis of the effects of varying testing percentage and tree depth on your results.  Also, include the graph for "all" with a max-depth of 6.  Comment on the findings obtained from the graph.

2. Analysis of the effects of number of estimators (trees) and max_depth on the importance of each feature.

Feel free to add charts and graphs to show your findings.  Remeber, a picture is worth a thousand words.

### Other modules
You will be makng use of scikit-learn in this project. You can do a global pip install of numpy or you can create a virtual environment just for this project if you prefer.  It is totally up to you.

## Deliverables
You will submit one zip file to eLearning. It will contain three files.
- **decision_tree.py** - your completed decision tree builder
- **random_forest.py** - your completed random forest generator
- **report.pdf** - your report (2 pages max) responding to the questions above.

Files must be named **EXACTLY**  as listed above or you will lose substantial points (40% or so.) This is a test as to whether you can follow simple instructions.

## Collaboration
You are expected to do your own work and you must turn in code that you have written yourself.  You are also encouraged to discuss how to do the project with your classmates.  You can learn a lot from discussing ideas and problems you are facing. You may not share any code.  You may not write code for somebody else.

You may make use of small snippets of code from online sources.  If you do so, you must put a comment before AND after the piece of code you used along withthe source:

Example:
```
# Code for this function taken from https://stackoverflow.com/postURL.....
xSquared = x * x
#End cited code
```
Failure to document your sources is plagiarism and if detected during the grading process, it may result in a zero on the project and it will definitely result in at least a major deduction.

## Avoiding Plagiarism
The easiest way to avoid plagiarism is to write code without referencing outside sources. This is, of course, impossible. Here are some guidelines as to how you can meet the requirement and still get help.

- Heuristic 1: Never hit "Copy" within a web search or conversation with an AI assistant. You can copy your own work into your conversation, but do not copy anything from the conversation back into your assignment. Instead, use your interaction with the web page or AI assistant as a learning experience, then let your assignment reflect your improved understanding.
- Heuristic 2: Do not have your assignment and the web page or AI agent open at the same time. Similar to above, use your conversation with the web page or AI as a learning experience, then close the interaction down, open your assignment, and let your assignment reflect your revised knowledge.
- Heuristic 3: When working with classmates, do not directly copy things that were discussed.  If there was a whiteboard involved, do not take a picture of it.  Instead, take notes from what is on the board that you can refer to as you do your own work.
## Grading
This project will be graded on how well your code generates the right solutions.  You will get minimal credit (20%) just for turning in something that looks like it should work and is on the right track. The remaining grade will be based on:
- Working decision tree solution (40%)
- Working random forest solution (40%)
- Report contents and analysis (20%)

Note that your code will be graded against different input values to verify a working solution. Your code needs to work with any reasonable set of inputs.  You are encouraged to try other input values to verify functionality.

## Getting help
You can talk amongst yourselves to solve the problem.  You can come and ask the professor for help.  He really does enjoy working with students to solve problems. There will also be a discord server setup for the course and you should have been invited to join.

## Completeness
This spec is believed to be complete.  If you have questions pelase ask.  There may be something missing. I will update the spec as omissions and errors are discovered. Your failure to ask does not excuse you from the consequences of doing something wrong.