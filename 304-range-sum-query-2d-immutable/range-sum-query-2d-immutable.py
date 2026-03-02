class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.Row = len(matrix)
        self.Col = len(matrix[0])
        self.matrix = matrix

        for r in range(self.Row):
            for c in range(self.Col):
                if 0 <= r-1 < self.Row:
                    self.matrix[r][c] += self.matrix[r-1][c]
                if 0 <= c-1 < self.Col:
                    self.matrix[r][c] += self.matrix[r][c-1]
                if 0 <= r-1 < self.Row and 0 <= c-1 < self.Col:
                    self.matrix[r][c] -= self.matrix[r-1][c-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
            res = self.matrix[row2][col2]
            if 0 <= row1-1 < self.Row:
                res -= self.matrix[row1-1][col2]
            if 0 <= col1-1 < self.Col:
                res -= self.matrix[row2][col1-1]
            if 0 <= row1-1 < self.Row and 0 <= col1-1 < self.Col:
                res += self.matrix[row1-1][col1-1]
    
            return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)