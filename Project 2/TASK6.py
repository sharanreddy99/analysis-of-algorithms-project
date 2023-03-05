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

    def main(self):
        # The first two loops fix the upper left corner for the given square plot.
        for rowStart in range(self.m):
            for colStart in range(self.n):
                # The next two loops fix the lower right corner for the square plot whose upper left corner is fixed.
                for rowEnd in range(rowStart, self.m):
                    for colEnd in range(colStart, self.n):
                        # Counter which stores the number of invalid individual plots in the chosen square plot.
                        inValidPlotsCount = 0

                        # The next two loops iterate over each square in the square plot of chosen dimensions and counts the plots which satisfy the min tree requirement.
                        for x in range(rowStart, rowEnd + 1):
                            for y in range(colStart, colEnd + 1):
                                if self.p[x][y] < self.h:
                                    inValidPlotsCount += 1

                        totRows = rowEnd - rowStart + 1
                        totCols = colEnd - colStart + 1

                        # We check whether the chosen plot is an optimal square plot satisfying the min tree requirement without crossing the exempted limit and store it if required.
                        if (
                            totRows == totCols
                            and inValidPlotsCount <= self.k
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
TIME COMPLEXITY  : O(m*n*m*n*m*n) = O(m^3 * n^3)
SPACE COMPLEXITY : O(1)

-----------------------------------------------------------------------------------------------------------------------------------------------------------
"""
