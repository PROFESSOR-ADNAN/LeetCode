class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        Row = len(matrix)
        Col = len(matrix[0])
        transpose = [[0] * Row for _ in range(Col)]
        for r in range(Row):
            for c in range(Col):
                transpose[c][r] = matrix[r][c]
        
        return transpose
        
        