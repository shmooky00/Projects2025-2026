
import sys, os, json
import solver as s



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#    DO NOT CHANGE ANY CODE BELOW THIS POINT
#
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Driver program to test above functions
if __name__ == '__main__':

    # Read filename to use for puzzle data
    filename = "data.json" if len(sys.argv) == 1 else sys.argv[1]

    # Verify puzzle data file exists
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "data\\" + filename
    abs_file_path = os.path.join(script_dir, rel_path)

    if os.path.isfile(abs_file_path):
        print(abs_file_path)
    else:
        print(f"file {abs_file_path} not found")
        exit()


    # Open JSON file and read into data
    f = open(abs_file_path)
    data = json.load(f)
    f.close()

    # Loop through puzzle list and validate / solve
    for i in data:
        BFS = s.solver(i['dim'], i['initial_state'])

        if not BFS.isValid():
            '''
            If puzzle isn't valid, print it to screen and print error message
            then go to the next puzzle
            '''
            print("**************************************")
            print(f"Puzzle {i['number']} not valid!")
            print("**************************************\n")
            continue

        print(f"----------------------- Solving puzzle {i['number']} -----------------------")

        # Valid puzzle at this point so solve the puzzle using breadth-first algorithm
        BFS.solvePuzzle()
        print(f"Breadth-first solution visited {BFS.nodeNumber} states to solve.")
        # BFS.printSolution()

        # Solve the puzzle using A* algorithm
        ASTAR = s.solver(i['dim'], i['initial_state'], True)
        ASTAR.solvePuzzle()
        print(f"A* solution visited {ASTAR.nodeNumber} states to solve.")
        ASTAR.printSolution()


    print("***** Thank you for playing *****")
