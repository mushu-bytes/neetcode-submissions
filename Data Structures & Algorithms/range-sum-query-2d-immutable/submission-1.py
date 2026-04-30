class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.preMatrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            rowCounter = 0
            for j in range(self.cols):
                rowCounter += matrix[i][j]
                self.preMatrix[i][j] = rowCounter
                if i > 0:
                    self.preMatrix[i][j] += self.preMatrix[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # return self.preMatrix[row2][col2] + self.preMatrix[row1][col1] - self.preMatrix[row2][col1] - self.preMatrix[row1][col2]
        body = self.preMatrix[row2][col2]
        left = self.preMatrix[row2][col1 - 1] if col1 > 0 else 0
        top  = self.preMatrix[row1 - 1][col2] if row1 > 0 else 0
        topleft = self.preMatrix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return body + topleft - left - top

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)