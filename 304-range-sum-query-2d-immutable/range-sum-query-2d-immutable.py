class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        R, C = len(matrix), len(matrix[0])
        self.prefixSum = [[0] * (C+1) for _ in range(R+1)]
        for r in range(R):
            for c in range(C):
                self.prefixSum[r+1][c+1] = self.prefixSum[r][c+1] + self.prefixSum[r+1][c] - self.prefixSum[r][c] + self.matrix[r][c]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ans = self.prefixSum[row2+1][col2+1] - self.prefixSum[row1][col2+1] - self.prefixSum[row2+1][col1] + self.prefixSum[row1][col1]
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)