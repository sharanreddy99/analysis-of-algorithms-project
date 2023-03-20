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

        # Stores the count of valid plots until each column.
        self.rowValidPlots = [0 for i in range(self.n)]

    def main(self):
        # The first two loops fix the upper left corner for the given square plot.
        for rowStart in range(self.m):
            for colStart in range(self.n):
                # clear the previously stored valid plots.
                for col in range(self.n):
                    self.rowValidPlots[col] = 0

                # count the number of valid plots with rowStart, colStart as the top left position of the region we are validating.
                for rowEnd in range(rowStart, self.m):
                    # we initialize the count of valid plots in the current row to 0.
                    currRowValidPlots = 0
                    for colEnd in range(colStart, self.n):
                        currRowValidPlots += (
                            1 if self.p[rowEnd][colEnd] >= self.h else 0
                        )

                        # we add the count of valid plots until ith column of current row to the count of valid plots until ith column of the previous rows.
                        self.rowValidPlots[colEnd] += currRowValidPlots

                        totRows = rowEnd - rowStart + 1
                        totCols = colEnd - colStart + 1

                        # We check whether the chosen plot is an optimal square plot satisfying the min tree requirement and store it if bigger than the previous maximal result.
                        if (
                            totRows == totCols
                            and self.rowValidPlots[colEnd] == totRows * totCols
                            and totRows > self.maxSquareLen
                        ):
                            self.resultIndicesArr[0] = rowStart + 1
                            self.resultIndicesArr[1] = colStart + 1
                            self.resultIndicesArr[2] = rowEnd + 1
                            self.resultIndicesArr[3] = colEnd + 1
                            self.maxSquareLen = totRows

        return self.resultIndicesArr


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
TIME COMPLEXITY  : O(m*n*(n + m*n) = O(m^2 * n^2 + m*n^2) = O(m^2 * n^2)
SPACE COMPLEXITY : O(n)

-----------------------------------------------------------------------------------------------------------------------------------------------------------
"""
