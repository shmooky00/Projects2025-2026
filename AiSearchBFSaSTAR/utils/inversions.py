# Python3 program to check if a given instance of N*N-1
# puzzle is solvable or not


# A utility function to count inversions in given
# array . Note that this function can be
# optimized to work in O(n Log n) time. The idea
# here is to keep code small and simple.

class Inversions:

    def __init__(self, n, puzzle):
        self.N = n
        self.puzzle = puzzle

    def getInvCount(self):
        arr = self.puzzle
        arr1=[]
        for y in arr:
            for x in y:
                arr1.append(x)
        arr=arr1
        inv_count = 0
        for i in range(self.N * self.N - 1):
            for j in range(i + 1,self.N * self.N):
                # count pairs(arr[i], arr[j]) such that
                # i < j and arr[i] > arr[j]
                if (arr[j] and arr[i] and arr[i] > arr[j]):
                    inv_count+=1

        return inv_count

    # find Position of blank from bottom
    def findXPosition(self):

        # start from bottom-right corner of matrix
        for i in range(self.N - 1,-1,-1):
            for j in range(self.N - 1,-1,-1):
                if (self.puzzle[i][j] == 0):
                    return self.N - i


    # This function returns true if given
    # instance of N*N - 1 puzzle is solvable
    def isSolvable(self):
        #puzzle = self.puzzle
        # N = self.N

        # Count inversions in given puzzle
        invCount = self.getInvCount()

        # If grid is odd, return true if inversion
        # count is even.
        if (self.N & 1):
            return not invCount % 2
            # return ~(invCount & 1)

        else:    # grid is even
            pos = self.findXPosition()
            if (pos & 1):
                return not invCount % 2
            else:
                return invCount % 2
                # return invCount & 1



# Driver program to test above functions
if __name__ == '__main__':

    dim = 4
    puzzle = [
        [12, 1, 10, 2,],
        [7, 11, 4, 14,],
        [5, 0, 9, 15,],
        [8, 13, 6, 3,],]

    p = Inversions(dim, puzzle)
    print("P1 Solvable") if  p.isSolvable() else print("P1 Not Solvable")

    dim = 3
    puzzle = [
        [4, 1, 2,],
        [7, 8, 6,],
        [5, 0, 3,],
    ]

    p = Inversions(dim, puzzle)
    print("P2 Solvable") if  p.isSolvable() else print("P2 Not Solvable")

    dim = 3
    puzzle = [
        [8, 1, 2,],
        [0, 4, 3,],
        [7, 6, 5,],
    ]

    p = Inversions(dim, puzzle)
    print("P3 Solvable") if  p.isSolvable() else print("P3 Not Solvable")

    dim = 4
    puzzle = [
        [3, 9,  1, 15,],
        [14, 11, 4, 6,],
        [13, 0, 10, 12,], # Value 0 is used for empty space
        [2, 7, 8, 5,],]

    p = Inversions(dim, puzzle)
    print("P4 Solvable") if  p.isSolvable() else print("P4 Not Solvable")