# Given a matrix p of m ×n integers (non-negative) representing the minimum number of trees that must be planted on each plot and an integer h (positive), find the bounding indices of a square area where all but the corner plots enclosed requires a minimum of h trees to be planted. The corner plots can have any number of trees required
# Design a Θ(m * n) time Dynamic Programming algorithm for solving Problem2 using Memoization (Top Down)
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

        # list of possible moves with respect to current plot to check for previously computed maximal square region lengths.
        self.moves = [
            # top left
            [-1, -1],
            # left
            [0, -1],
            # top
            [-1, 0],
        ]

        self.initDPArray()

    def initDPArray(self):
        # DP[i,j] indicates the largest possible square length having bottom right corner as i,j with corner exemptions.
        self.dp = [[0 for x in range(self.n + 1)] for y in range(self.m + 1)]

        # validCountArr stores the no of plots satisfying the min tree requirement in the given region bounded by top left (0, 0)
        # and bottom right (i, j)
        self.validCountArr = [[0 for i in range(self.n + 1)] for j in range(self.m + 1)]

        # We compute the validCount bounded by [0,0] and [i,j] based on the previously computed values.
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                self.validCountArr[i][j] = (
                    self.validCountArr[i][j - 1]
                    + self.validCountArr[i - 1][j]
                    - self.validCountArr[i - 1][j - 1]
                    + (1 if self.p[i - 1][j - 1] >= self.h else 0)
                )

    # getTopLeft returns the top left corner for a given bottom right position based on the distance provided.
    def getTopLeft(self, rowEnd, colEnd, dist):
        return rowEnd - dist + 1, colEnd - dist + 1

    # getValidCount returns the the no of valid plots in the region bounded by topleft corner [rowStart, colStart] and
    # bottom right corner [rowEnd, colEnd]
    def getValidCount(self, rowStart, colStart, rowEnd, colEnd):
        validCount = self.validCountArr[rowEnd][colEnd]
        validCount -= self.validCountArr[rowStart - 1][colEnd]
        validCount -= self.validCountArr[rowEnd][colStart - 1]
        validCount += self.validCountArr[rowStart - 1][colStart - 1]
        return validCount

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

    # validateAndStoreRegion checks if the given region satisfies the min trees requirement and updates the result if we get a maximal square region.
    def validateAndStoreRegion(self, rowEnd, colEnd, dist, k):
        rowStart, colStart = self.getTopLeft(rowEnd, colEnd, dist)
        # if the newly found top left corner is a valid position, process the region.
        if rowStart > 0 and colStart > 0 and rowStart <= rowEnd and colStart <= colEnd:
            validCount = self.getValidCount(rowStart, colStart, rowEnd, colEnd)
            exemptedCount = self.getExemptedCellsCount(
                rowStart, colStart, rowEnd, colEnd
            )

            totRows = rowEnd - rowStart + 1
            totCols = colEnd - colStart + 1

            if validCount + exemptedCount >= totRows * totCols:
                self.dp[rowEnd][colEnd] = max(self.dp[rowEnd][colEnd], dist)

                # if the area enclosed by the boundaries forms a square region and is optimal than the previous result, store it.
                if totRows == totCols and totRows > self.maxSquareLen:
                    self.resultIndicesArr[0] = rowStart
                    self.resultIndicesArr[1] = colStart
                    self.resultIndicesArr[2] = rowEnd
                    self.resultIndicesArr[3] = colEnd
                    self.maxSquareLen = totRows
            else:
                # We ensure that we have processed the current cell by setting it to 0 which by default is -1.
                self.dp[rowEnd][colEnd] = max(self.dp[rowEnd][colEnd], 0)

    def compute(self, rowEnd, colEnd, k):
        if rowEnd == 0 or colEnd == 0:
            self.dp[rowEnd][colEnd] = 0
            return 0

        # If we come across a subproblem which was solved earlier, we return the result directly.
        if self.dp[rowEnd][colEnd] != -1:
            return self.dp[rowEnd][colEnd]

        for x, y in self.moves:
            # maximum square area formed by the plot, which is adjacent to the current bottom right plot position, with atmost k exemptions.
            length = self.compute(rowEnd + x, colEnd + y, k)

            # Store the length of the optimal square region ending at current cell based on the previously obtained length and atmost k excemptions.
            for inc in range(-1, 2, 1):
                self.validateAndStoreRegion(rowEnd, colEnd, length + inc, k)

        return self.dp[rowEnd][colEnd]

    def main(self):
        self.compute(self.m, self.n, self.k)
        return self.resultIndicesArr


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
TIME COMPLEXITY  : O(m*n)
SPACE COMPLEXITY : O(m*n)

-----------------------------------------------------------------------------------------------------------------------------------------------------------
"""
