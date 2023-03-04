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

    def main(self):
        # The first two loops fix the upper left corner for the given square plot.
        for rowStart in range(self.m):
            for colStart in range(self.n):

                # validPlotsCount stores the number of valid individual plots in the chosen square plots.
                validPlotsCount = 0

                # The next two loops fix the lower right corner for the square plot whose upper left corner is fixed and count the plots which satisfy the requirement.
                rowEnd = rowStart
                colEnd = colStart

                while rowEnd < self.m and colEnd < self.n:
                    # We check the rightMost column alongside previously chosen square plot.
                    for row in range(rowStart, rowEnd):
                        if self.p[row][colEnd] >= self.h:
                            validPlotsCount += 1

                    # We check the bottomMost row alongside previously chosen square plot.
                    for col in range(colStart, colEnd + 1):
                        if self.p[rowEnd][col] >= self.h:
                            validPlotsCount += 1

                    totRows = rowEnd - rowStart + 1
                    totCols = colEnd - colStart + 1

                    # We check whether the chosen plot is an optimal square plot satisfying the min tree requirement and store it if required.
                    if (
                        totRows == totCols and validPlotsCount == totRows *
                            totCols and totRows > self.maxSquareLen
                    ):
                        self.resultIndicesArr[0] = rowStart + 1
                        self.resultIndicesArr[1] = colStart + 1
                        self.resultIndicesArr[2] = rowEnd + 1
                        self.resultIndicesArr[3] = colEnd + 1
                        self.maxSquareLen = totRows

                    rowEnd += 1
                    colEnd += 1

        return self.resultIndicesArr


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
TIME COMPLEXITY  : O(m*n*m*n) = O(m^2 * n^2)
SPACE COMPLEXITY : O(1)

-----------------------------------------------------------------------------------------------------------------------------------------------------------
"""
