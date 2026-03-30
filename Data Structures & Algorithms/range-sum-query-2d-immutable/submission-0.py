class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.prefixMatrix = [[0] * (COLS + 1) for _ in range(ROWS+1)]
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.prefixMatrix[r][c+1]
                self.prefixMatrix[r+1][c+1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefixMatrix[row2+1][col2+1]
        above = self.prefixMatrix[row1][col2 + 1]
        left = self.prefixMatrix[row2+1][col1]
        topLeft = self.prefixMatrix[row1][col1]
        return total - above - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)