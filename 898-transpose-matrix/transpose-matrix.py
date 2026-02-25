class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        Row = len(matrix)
        Col = len(matrix[0])

        transpose = [[0 for _ in range(Row)] for _ in range(Col)]

        for r in range(Row):
            for c in range(Col):
                transpose[c][r] = matrix[r][c]
        
        return transpose