# Kalman Filters in Two Dimensions
This project will expand upon your knowledge of Kalman Filters in a one-dimensional environment by implementing code to support motion in a two-dimensional (x,y) plane.

## Overview
You will be provided with a list of measurements in the following format:
```
[[1,1], [2,4], [3,7], .....]
```
where each sub-list contains the next x,y observation.

Your code will loop through the list of measurements and produce the final position and velocity as calculated by your Kalman Filter program. You will also print out the final covariance matrix to show how it has changed from the intial matrix that you supply.

## The Code
You are being provided two files for the project.

**kalman_1D_matrix.py** - This file provides the matrices for a one-dimensional Kalman Filter.  You will want to implement the proper equations to get the output as described in the file.  This program is **30%** of the grade

**kalman_2D_matrix.py** - This file will be your implementation of the two-dimensional version of the Kalman Filter.  Of course you are free to re-use the work from the 1D problem and modify it accordingly. This program is **50%** of the grade.

Note that in this file there are a couple of lines of code that can generate gaussian noise to apply to the measurements.  You will need to implement this capability in order to complete the report.

To run your code for testing purposes you will do this:
```
python kalman_1D_matrix.py
python kalman_2D.py
```
## The Report
You will also submit a report (worth **20%** of the grade) that answers the following questions:

1. What effect does the initial covariance matrix have on the answer to the problem? You must provide data to back-up your claims.  An easy way to do this is to use a matrix P that has different initial values and observe how the output of the program is affected.

2. What effect does the addition of gaussian noise to the measurements have on the resulting final position. Again, you must provide data to back-up your claims.  You will need to do this from two perspectives:
   - Run your code multiple times for a given noise value and capture the output. Provide a table or graph that shows how the final results vary (or not) when noise is added.
   - Run your code with multiple levels of noise (alter the sigma value) and show how that affects the results.

3. With regards to the findings in part 2, explain what the gaussian noise is simulating in this project. (i.e., what real-life physical phenomena is the noise a substitute for.)

Feel free to add charts and graphs to show your findings.  Remeber, a picture is worth a thousand words.

### Other modules
You will be makng use of nmumpy in this project. You can do a global pip install of numpy or you can create a virtual environment just for this project if you prefer.  It is totally up to you.

## Deliverables
You will submit one zip file to eLearning. It will contain three files.
- **kalman_1D_matrix.py** - your completed 1D matrix implementation
- **kalman_2D_matrix.py** - your completed 2D matrix implementation
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
- Working 1D solution (30%)
- Working 2D solution (50%)
- Report contents and analysis (20%)

Note that your code will be graded against different input values to verify a working solution. Your code needs to work with any reasonable set of inputs.  You are encouraged to try other input values to verify functionality.

## Getting help
You can talk amongst yourselves to solve the problem.  You can come and ask the professor for help.  He really does enjoy working with students to solve problems. There will also be a discord server setup for the course and you should have been invited to join.

## Completeness
This spec is believed to be complete.  If you have questions pelase ask.  There may be something missing. I will update the spec as omissions and errors are discovered. Your failure to ask does not excuse you from the consequences of doing something wrong.