# Search - 8 Puzzle and 15 Puzzle solver
This project will implement two search algorithms to solve an "n puzzle." You may have played with
these puzzles when you were younger. You have a square grid of number sliders and one blank space.
The goal of the game is to slide the tiles around the board until you get the tiles in ascending numeric
order with the blank space in the bottom right corner.
## Example

```
Given this input puzzle         Produce this solution:
-------------                   -------------
| 4 | 1 | 2 |                   | 1 | 2 | 3 |
-------------                   -------------
| 7 | 8 | 6 |                   | 4 | 5 | 6 |
-------------                   -------------
| 5 | X | 3 |                   | 7 | 8 | X |
-------------                   -------------
```

## The Code
You are being provided a a python file called solver.py that is called from n_puzzle.py. This starter code provides a standard starting
point to easily implement, run and eventually grade the project. n_puzzle.py will read puzzle data from the data.json file as a puzzle source.

To run the code you will do this:
```
python n_puzzle.py
```

You may create your own .json file with additional puzzles for testing purposes. To use that file instead of the default data file, put the file in the data directory and run this:

```
python n_puzzle.py yourfilename.json
```

When I grade the project, I will use a different .json file with different puzzles in it that are known to work.  By work, I mean are found to be invalid or will solve properly.

### Project Methods
In the solver class in solver.py, there are a number of methods that you will have to write the code for.  Note that you can add any additional methods that you like but you must not eliminate any of the provided methods.  The test script will call these methods and it expects them to provide the designated functions.
- **__init__()** - pythons version of a constructor.  Pretty self explanatory and partially done for you. Feel free to add other stuff to here as necessary.
- **isValid()** - This method will take the loaded puzzle and verify that it can be solved. An inversions.py file is provided that has a class that you can call to test the initial puzzle state for validity.
- **solvePuzzle()** - Here you will implement the breadth first algorithm to solve the puzzle. Once that works, you can modify the code to also work with A* since the methods are similar.
- **printSolution()** - This method will print the nodes (in a format similar to what is shown above) ideally it prints the first state to last but printing in reverse order would be acceptable too. I should be able to take a real puzzle in the initial state, follow what you print and end up with a solved puzzle.
- **printPuzzle()** - this just prints a puzzle configuration to the screen. 
### Other modules
You may use any python modules that are part of the standard python library.  They aren't needed but you may make use of them.  Obviously, you may not use any module that provides a breadth first or A* search method.  Your job is to write theses methods as part of the assignment. Also, you may not copy any of them either.  See the plagiarism discussion, below.
## Deliverables
You will submit one file to eLearning.  The file will be the **solver.py** file.  **DO NOT zip this file** and then upload it. Just upload the file. It must be **EXACTLY** this name or you will lose substantial points (50% or so.) This is a test as to whether you can follow simple instructions.

Your code will be submitted to Turnitin to do a similarity check for plagiarism and inappropriate collaboration.
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
This project will be graded on how well your code solves the provided puzzles.  You will get minimal credit (20% or so) just for turning in something that looks like it should work and is on the right track. The remaining grade will be based on:
- Solving the puzzle (or identifying that it is invalid)
- Printing each node from initial state to final solution
- Accurately counting how many steps were involved.  For purposes of this project count all steps from initial state to final solution.  For example, if you start solving, make 5 moves and end up with the solution, you will have 6 steps.  The initial configuration plus the number of moves you made to get to the final solution. This also implies that when you print each node in the solution, you will be printing six nodes.

Net of all of that is that your code needs to work when you submit it.
## Getting help
You can talk amongst yourselves to solve the problem.  You can come and ask the professor for help.  He really does enjoy working with students to solve problems. There will also be a discord server setup for the course and you should have been invited to join.

## Completeness
This spec is believed to be complete.  If you have questions pelase ask.  There may be something missing. I will update the spec as omissions and errors are discovered. Your failure to ask does not excuse you from the consequences of doing something wrong.

## Project Notes
These are notes collected each semester that will help clarify the project.

- Although the code could solve every valid puzzle, the complexity of the solution (how mixed up it is), the space and/or time complexity will make solving the puzzle impractical on our computers. With that in mind, your solving loop should have a "break out" that aborts the solution after 75,000 iterations.  Your code should produce a message that states that it is a valid puzzle but the iteration limit was reached before finding the solution.