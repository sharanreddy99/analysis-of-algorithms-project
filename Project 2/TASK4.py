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
    def validateAndStoreRegion(self, rowEnd, colEnd, dist):
        rowStart, colStart = self.getTopLeft(rowEnd, colEnd, dist)
        # if the newly found top left corner is a valid position, process the region.
        if rowStart > 0 and colStart > 0 and rowStart <= rowEnd and colStart <= colEnd:
            validCount = self.getValidCount(rowStart, colStart, rowEnd, colEnd)
            exemptedCount = self.getExemptedCellsCount(
                rowStart, colStart, rowEnd, colEnd
            )

            # if the region formed is a valid square plot with corner exemptions and is bigger than the previous maximal result, store it.
            if validCount + exemptedCount >= dist * dist and dist > self.maxSquareLen:
                self.resultIndicesArr[0] = rowStart
                self.resultIndicesArr[1] = colStart
                self.resultIndicesArr[2] = rowEnd
                self.resultIndicesArr[3] = colEnd
                self.maxSquareLen = dist

    def main(self):
        # fix the top left corner of the required region at each point in the grid.
        for rowStart in range(1, self.m + 1):
            for colStart in range(1, self.n + 1):
                # Pull the bottom right corner diagonally and validate the region and store if maximal square region.
                for inc in range(min(self.m - rowStart + 1, self.n - colStart + 1)):
                    rowEnd, colEnd = rowStart + inc, colStart + inc
                    self.validateAndStoreRegion(rowEnd, colEnd, inc + 1)
        return self.resultIndicesArr


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
TIME COMPLEXITY  : O(m * n * min(m,n))
SPACE COMPLEXITY : O(m*n)

-----------------------------------------------------------------------------------------------------------------------------------------------------------
"""
