# Given a matrix p of m ×n integers (non-negative) representing the minimum number of trees that must be planted on each plot and an integer h (positive), find the bounding indices of a square area where all but the corner plots enclosed requires a minimum of h trees to be planted. The corner plots can have any number of trees required
# Design a Θ(m * n^2) time Dynamic Programming algorithm for solving Problem2
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

        self.initDPArray()

    def initDPArray(self):
        self.dp = [[0 for i in range(self.n + 1)] for j in range(self.m + 1)]

        # dp[i,j] gives the count of plots which satisfy the min tree requirement for ith row untill jth house.
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                self.dp[i][j] = self.dp[i][j - 1] + (
                    1 if self.p[i - 1][j - 1] >= self.h else 0
                )

    # getExemptionCellsCount returns the count of invalid plots from the corners of a given region which can be exempted.
    def getExemptedCellsCount(self, rowStart, colStart, rowEnd, colEnd):
        count = 0
        if self.p[rowStart - 1][colStart - 1] < self.h:
            count += 1

        if self.p[rowStart - 1][colEnd - 1] < self.h:
            count += 1

        if self.p[rowEnd - 1][colStart - 1] < self.h:
            count += 1

        if self.p[rowEnd - 1][colEnd - 1] < self.h:
            count += 1

        return count

    def main(self):
        for cLeft in range(1, self.n + 1):
            for cRight in range(cLeft, self.n + 1):
                validPlotsCount = 0
                startRow = 1
                for row in range(1, self.m + 1):
                    tempCount = self.dp[row][cRight] - self.dp[row][cLeft - 1]

                    validPlotsCount += tempCount
                    exemptionCount = self.getExemptedCellsCount(
                        startRow, cLeft, row, cRight
                    )

                    totRows = row - startRow + 1
                    totCols = cRight - cLeft + 1

                    # Update the new start row if we don't have a plot with valid number of trees after exemptions.
                    if validPlotsCount + exemptionCount < totRows * totCols:
                        startRow = row
                        validPlotsCount = tempCount

                    # We check whether the chosen plot is an optimal square plot satisfying the min tree requirement and store it if required.
                    if (
                        totRows == totCols
                        and (validPlotsCount + exemptionCount) >= totRows * totCols
                        and totRows > self.maxSquareLen
                    ):
                        self.maxSquareLen = row
                        self.resultIndicesArr[0] = startRow
                        self.resultIndicesArr[1] = cLeft
                        self.resultIndicesArr[2] = row
                        self.resultIndicesArr[3] = cRight

        return self.resultIndicesArr


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
TIME COMPLEXITY  : O(m * n)
SPACE COMPLEXITY : O(n)

-----------------------------------------------------------------------------------------------------------------------------------------------------------
"""
