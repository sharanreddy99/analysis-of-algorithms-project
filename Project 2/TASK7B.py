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

        self.initDPArray()

    def initDPArray(self):
        self.dp = [[0 for x in range(self.n + 1)] for y in range(self.m + 1)]

        self.invalidCountArr = [
            [0 for i in range(self.n + 1)] for j in range(self.m + 1)
        ]

        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                self.invalidCountArr[i][j] = (
                    self.invalidCountArr[i][j - 1]
                    + self.invalidCountArr[i - 1][j]
                    - self.invalidCountArr[i - 1][j - 1]
                    + (1 if self.p[i - 1][j - 1] < self.h else 0)
                )

    def getTopLeft(self, rowEnd, colEnd, dist):
        return rowEnd - dist + 1, colEnd - dist + 1

    def getInvalidCount(self, rowStart, colStart, rowEnd, colEnd):
        invalidCount = self.invalidCountArr[rowEnd][colEnd]
        if rowStart - 1 >= 0:
            invalidCount -= self.invalidCountArr[rowStart - 1][colEnd]

        if colStart - 1 >= 0:
            invalidCount -= self.invalidCountArr[rowEnd][colStart - 1]

        if rowStart - 1 >= 0 and colStart - 1 >= 0:
            invalidCount += self.invalidCountArr[rowStart - 1][colStart - 1]

        return invalidCount

    def computeValidSquare(self, rowEnd, colEnd, dist, k):
        rowStart, colStart = self.getTopLeft(rowEnd, colEnd, dist)
        if rowStart > 0 and colStart > 0:
            invalidCount = self.getInvalidCount(rowStart, colStart, rowEnd, colEnd)
            if invalidCount <= k:
                self.dp[rowEnd][colEnd] = max(self.dp[rowEnd][colEnd], dist)
                totRows = rowEnd - rowStart + 1
                totCols = colEnd - colStart + 1

                if totRows == totCols and totRows > self.maxSquareLen:
                    self.resultIndicesArr[0] = rowStart
                    self.resultIndicesArr[1] = colStart
                    self.resultIndicesArr[2] = rowEnd
                    self.resultIndicesArr[3] = colEnd
                    self.maxSquareLen = totRows

    def main(self):
        for k in range(self.k + 1):
            for rowEnd in range(1, self.m + 1):
                for colEnd in range(1, self.n + 1):
                    dist1 = self.dp[rowEnd - 1][colEnd - 1]
                    dist2 = self.dp[rowEnd][colEnd]
                    dist3 = (
                        min(self.dp[rowEnd][colEnd - 1], self.dp[rowEnd - 1][colEnd])
                        + 1
                    )
                    self.computeValidSquare(rowEnd, colEnd, dist1 + 1, k)
                    self.computeValidSquare(rowEnd, colEnd, dist2 + 1, k)
                    self.computeValidSquare(rowEnd, colEnd, dist3, k)

        return self.resultIndicesArr


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
TIME COMPLEXITY  : O(n*n*m)
SPACE COMPLEXITY : O(m*n)

-----------------------------------------------------------------------------------------------------------------------------------------------------------
"""
