class Main:
    def __init__(self, m, n, h, k, p):
        # No of rows
        self.m = m

        # No of cols
        self.n = n

        # Min number of trees
        self.h = h

        # Trees planted on each plot
        self.p = p

        # No of exempted square plots
        self.k = k

        # Array which stores the top left and bottom right indices sequentially
        self.resultIndicesArr = [-1, -1, -1, -1]

        # Size of the maximal square plot
        self.maxSquareLen = 0

        # list of possible moves with respect to current plot to check for previously computed maximal square region lengths.
        self.moves = [
            # top left with atmost k exemptions
            [-1, -1, 0],
            # top with atmost k exemptions
            [-1, 0, 0],
            # left with atmost k exemptions
            [0, -1, 0],
            # top left with atmost k - 1 exemptions
            [-1, -1, -1],
            # top with atmost k - 1 exemptions
            [-1, 0, -1],
            # left with atmost k - 1 exemptions
            [0, -1, -1],
            # current  with atmost k - 1 exemptions
            [0, 0, -1],
        ]

        self.initDPArray()

    def initDPArray(self):
        # intiialize the memorization table with m,n in the x and y dimensions respectively.
        self.dp = [
            [[-1 for x in range(self.n + 1)] for y in range(self.m + 1)]
            for k in range(self.k + 1)
        ]

        # invalidCountArr stores the no of plots with minTrees less than the minimum requirement in a given region bounded by top left (0, 0)
        # and bottom right (i, j)
        self.invalidCountArr = [
            [0 for i in range(self.n + 1)] for j in range(self.m + 1)
        ]

        # We compute the invalidCount bounded by [0,0] and [i,j] based on the previously computed values.
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                self.invalidCountArr[i][j] = (
                    self.invalidCountArr[i][j - 1]
                    + self.invalidCountArr[i - 1][j]
                    - self.invalidCountArr[i - 1][j - 1]
                    + (1 if self.p[i - 1][j - 1] < self.h else 0)
                )

    # getTopLeft returns the top left corner for a given bottom right position based on the distance provided.
    def getTopLeft(self, rowEnd, colEnd, dist):
        return rowEnd - dist + 1, colEnd - dist + 1

    # getInvalidCount returns the the no of invalid plots in the region bounded by topleft corner [rowStart, colStart] and
    # bottom right corner [rowEnd, colEnd]
    def getInvalidCount(self, rowStart, colStart, rowEnd, colEnd):
        invalidCount = self.invalidCountArr[rowEnd][colEnd]
        invalidCount -= self.invalidCountArr[rowStart - 1][colEnd]
        invalidCount -= self.invalidCountArr[rowEnd][colStart - 1]
        invalidCount += self.invalidCountArr[rowStart - 1][colStart - 1]
        return invalidCount

    # validateAndStoreRegion checks if the given region satisfies the min trees requirement and updates the result if we get a maximal square region.
    def validateAndStoreRegion(self, rowEnd, colEnd, dist, k):
        rowStart, colStart = self.getTopLeft(rowEnd, colEnd, dist)
        # if the newly found top left corner is a valid position, process the region.
        if rowStart > 0 and colStart > 0:
            invalidCount = self.getInvalidCount(rowStart, colStart, rowEnd, colEnd)
            if invalidCount <= k:
                self.dp[k][rowEnd][colEnd] = max(self.dp[k][rowEnd][colEnd], dist)
                totRows = rowEnd - rowStart + 1
                totCols = colEnd - colStart + 1

                # if the area enclosed by the boundaries forms a square region and is optimal than the previous result, store it.
                if totRows == totCols and totRows > self.maxSquareLen:
                    self.resultIndicesArr[0] = rowStart
                    self.resultIndicesArr[1] = colStart
                    self.resultIndicesArr[2] = rowEnd
                    self.resultIndicesArr[3] = colEnd
                    self.maxSquareLen = totRows
            else:
                # We ensure that we have processed the current cell by setting it to 0 which by default is -1.
                self.dp[k][rowEnd][colEnd] = max(self.dp[k][rowEnd][colEnd], 0)

    def compute(self, rowEnd, colEnd, k):
        if rowEnd == 0 or colEnd == 0:
            self.dp[k][rowEnd][colEnd] = 0
            return 0

        # If we come across a subproblem which was solved earlier, we return the result directly.
        if self.dp[k][rowEnd][colEnd] != -1:
            return self.dp[k][rowEnd][colEnd]

        for x, y, z in self.moves:
            if k + z >= 0:
                # maximum square area formed by the plot, which is adjacent to the current bottom right plot position, with atmost k exemptions.
                length = self.compute(rowEnd + x, colEnd + y, k + z)

                # Store the length of the optimal square region ending at current cell based on the previously obtained length and atmost k excemptions.
                self.validateAndStoreRegion(rowEnd, colEnd, length + 1, k)

        return self.dp[k][rowEnd][colEnd]

    def main(self):
        self.compute(self.m, self.n, self.k)
        return self.resultIndicesArr


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
TIME COMPLEXITY  : O(k*m*n)
SPACE COMPLEXITY : O(k*m*n)

-----------------------------------------------------------------------------------------------------------------------------------------------------------
"""
