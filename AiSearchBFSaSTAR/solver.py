'''
Implement various search algorithms to solve an n-puzzle of dimension N.

Input - Dimension N of a puzzle and the puzzle of size NxN seeded with random
    seuqential integers from 1 to N^2 - 1

Outputs for each puzzle in :

    1. A solved puzzle or indication that the input puzzle was invalid.

    2. Intermediate states (steps taken) to solve the puzzle.

Potential limitations:

    1. Puzzles larger that 3x3 may not solve due to memory constraints vs. number
        of states to store

Your code:
    1. The constructor takes three parameters - the dimensions of the puzzle (3 for 3x3
        or 4 for 4x4), the puzzle's initial state in a 2D list (list of lists) and a flag for
        the algorithm (Breadth-first or A*.) Default is BFS.

    2. You should not need to change any code outside of this file.  If you think you do,
       plesae see the instructor to review and approve.

    3. You will implement the code for breadthFirst(), aStar(), printSolution(), and printPuzzle()
'''

from pprint import pprint
from utils.inversions import Inversions
import copy
from collections import deque

#https://aima.cs.berkeley.edu/ (referenced by the book)

#my code works for puzzle 3, im not sure if its intentional but the bfs solves it 
# after like 5 minutes, it visits 60636 states, so i beleive it solves correctly

class solver:

    # The sequential number of each node to identify parent node
    # Used for printing the solution sequence at the end
    nodeNumber = 0

    def __init__(self, dimensions, puzzle, aStar = False ):
        '''
        Constructor that loads the dimensions and puzzle data
        '''
        self.dim = dimensions
        self.aStar = aStar
        self.puzzle = puzzle

        # You may add more code here

        self.solutionPath = None
        self.nodeNumber = 0
        self.maxIterations = 75000

        self.goalState = tuple(range(1, self.dim * self.dim)) + (0,)


    def isValid(self):
        '''
        Validate the initial state of the puzzle
        '''

        inversionCheck = Inversions(self.dim, self.puzzle)
        return inversionCheck.isSolvable()

    def solvePuzzle(self):
        '''
        Solve the puzzle using the Breadth First or A* algorithm
        Algorithm used will be defined by the boolean self.aStar
            - False - use BFS
            - True use A*
        '''
        # You will add code here

        #converting puzzle to tuple
        initialState = []

        for row in self.puzzle:
        
            for item in row:
                initialState.append(item)
        initialState = tuple(initialState)

        if not self.isValid():
            print("Not a valid puzzle.")
            return None

        #choose the algorithm and prints to console in repsonse
        if self.aStar:
            self.aStarSearch(initialState)
        else:
            self.breadthFirst(initialState)
        
    def breadthFirst(self, initialState):

        openList = [initialState] #unexplored
        closedList = [] #already explored
        actions = {initialState: []} #actions to reach state

        self.nodeNumber = 0
    
        while openList and self.nodeNumber < self.maxIterations:
            currentState = openList.pop(0)
            closedList.append(currentState)
            self.nodeNumber += 1
        
            if currentState == self.goalState:
                self.solutionPath = actions[currentState]
                return
        
            for action in self.getValidActions(currentState):
                newState = self.applyAction(currentState, action)
            
                if newState not in closedList and newState not in openList:
                    openList.append(newState)
                    actions[newState] = actions[currentState] + [action]

        self.solutionPath = None

    def aStarSearch(self, initialState):

        openList = [(self.calcHeuristic(initialState), initialState)]
        closedList = []
        actions = {initialState: []} 

        self.nodeNumber = 0

        #loop until empty openlist or max iterations hit
        while openList and self.nodeNumber < self.maxIterations:
            openList.sort()
            cost, currentState = openList.pop(0)
            closedList.append(currentState)
            self.nodeNumber += 1

            if currentState == self.goalState:
                self.solutionPath = actions[currentState]
                return

            for action in self.getValidActions(currentState):
                newState = self.applyAction(currentState, action)

                #check if the state is not in closed list
                if newState not in closedList and newState not in openList:
                    gCost = len(actions[currentState]) + 1
                    hCost = self.calcHeuristic(newState)
                    fCost = gCost + hCost
                    
                    #check if the state is not in open list
                    inOpenList = False
                    for cost, state in openList:
                        if state == newState:
                            inOpenList = True
                            break
                    
                    if not inOpenList:
                        openList.append((fCost, newState))
                        actions[newState] = actions[currentState] + [action]
        
        self.solutionPath = None

    #this was inspired in this link under the actions method in the eightpuzzle class-----------------------
    #https://github.com/aimacode/aima-python/blob/master/search.py
    def getValidActions(self, state):

        blankPos = state.index(0)
        actions = []
    
        if blankPos >= self.dim:
            actions.append('UP')
    
        if blankPos < self.dim * (self.dim - 1):
            actions.append('DOWN')
    
        if blankPos % self.dim != 0:
            actions.append('LEFT')
    
        if blankPos % self.dim != self.dim - 1:
            actions.append('RIGHT')
    
        return actions

    def applyAction(self, state, action):

        #this makes a copy of the state and figures out where to move the blank
        newState = list(state)
        blankPos = newState.index(0)
    
        if action == 'UP':
            newPos = blankPos - self.dim
        elif action == 'DOWN':
            newPos = blankPos + self.dim
        elif action == 'LEFT':
            newPos = blankPos - 1
        elif action == 'RIGHT':
            newPos = blankPos + 1
    
        newState[blankPos] = newState[newPos]
        newState[newPos] = 0
    
        return tuple(newState)

    def applyActionTo2D(self, puzzle2D, action):

        #convert 2d to 1d
        state1D = tuple([item for row in puzzle2D for item in row])
    
        newState1D = self.applyAction(state1D, action)
    
        newPuzzle = []

        #back to 2d
        for i in range(self.dim):
            row = []
            for j in range(self.dim):
                row.append(newState1D[i * self.dim + j])
            newPuzzle.append(row)
    
        return newPuzzle
        
        #end of inspo --------------------------------------------------------

    def calcHeuristic(self, state):

        totalDistance = 0

        for i in range(len(state)):

            if state[i] != 0: #disregard blank tile

                goalPostion = self.goalState.index(state[i])

                #convert 1d into 2d coordinates
                currentRow = i // self.dim
                currentCol = i % self.dim
                goalRow = goalPostion // self.dim
                goalCol = goalPostion % self.dim
                
                #manhattan modified from astar example
                totalDistance += abs(currentRow - goalRow) + abs(currentCol - goalCol)
        
        return totalDistance
        

    def printSolution(self):
        '''
        Print the nodes traversed to get to the solution
        '''
        # You will add code here
        
        if not self.solutionPath:
            print("No solution found.")
            return

        print(f"The solution was found in {len(self.solutionPath)} moves.")
        print(f"Nodes expanded: {self.nodeNumber}")

        currentState = [row[:] for row in self.puzzle] #initial state to 2d

        print("Node 0: Initial state")
        self.printPuzzle()
        print()
        
        #applies the actions previously made and prints result
        for i, action in enumerate(self.solutionPath, 1):
            print(f"State {i}: Moved {action}")

            currentState = self.applyActionTo2D(currentState, action)
            self.printPuzzleFrom2D(currentState)
            print()

    def printPuzzle(self):
        '''
        Print the puzzle configuration
        '''
        # You will add code here
        
        self.printPuzzleFrom2D(self.puzzle)

    def printPuzzleFrom2D(self, puzzle2D):
        
        for row in puzzle2D:
            print(' '.join(str(num) for num in row)) #makes the new states output look clean in console
