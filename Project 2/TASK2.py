# Given a matrix p of m ×n integers (non-negative) representing the minimum number of trees that must be planted on each plot and an integer h (positive), find the bounding indices of a square area where each plot enclosed requires a minimum of h trees to be planted
# Design a Θ(m^2 * n^2) time algorithm for solving Problem1
class Main:
    def __init__(self, m, n, h, p):
        # No of rows
        self.m = m

        # No of cols
        self.n = n

        # Min number of trees
        self.h = h

        # Trees planted on each plot
        self.p = p

        # Array which stores the top left and bottom right indices sequentially
        self.resultIndicesArr = [-1, -1, -1, -1]

        # Size of the maximal square plot
        self.maxSquareLen = 0

        # Stores the count of valid plots for each column.
        self.colSum = [[0 for i in range(self.n + 1)] for j in range(2)]

    def main(self):
        # The first two loops fix the upper left corner for the given square plot.
        for rowStart in range(1, self.m + 1):
            for colStart in range(1, self.n + 1):
                # Reset column sum
                for x in range(2):
                    for y in range(self.n + 1):
                        self.colSum[x][y] = 0

                # The next two loops fix the lower right corner for the square plot whose upper left corner is fixed and compute the no of mintree plots
                # in the given square based on the precomputed value from the previous row.
                for rowEnd in range(rowStart, self.m + 1):
                    for colEnd in range(colStart, self.n + 1):
                        self.colSum[rowEnd % 2][colEnd] = (
                            self.colSum[rowEnd % 2][colEnd - 1]
                            + self.colSum[(rowEnd - 1) % 2][colEnd]
                            - self.colSum[(rowEnd - 1) % 2][colEnd - 1]
                            + (1 if self.p[rowEnd - 1][colEnd - 1] >= self.h else 0)
                        )

                        totRows = rowEnd - rowStart + 1
                        totCols = colEnd - colStart + 1

                        # We check whether the chosen plot is an optimal square plot satisfying the min tree requirement and store it if required.
                        if (
                            totRows == totCols
                            and self.colSum[rowEnd % 2][colEnd] == totRows * totCols
                            and totRows > self.maxSquareLen
                        ):
                            self.resultIndicesArr[0] = rowStart
                            self.resultIndicesArr[1] = colStart
                            self.resultIndicesArr[2] = rowEnd
                            self.resultIndicesArr[3] = colEnd
                            self.maxSquareLen = totRows

        return self.resultIndicesArr


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
TIME COMPLEXITY  : O(m*n*m*n + m*n*n) = O(m^2 * n^2)
SPACE COMPLEXITY : O(n)

-----------------------------------------------------------------------------------------------------------------------------------------------------------
"""
