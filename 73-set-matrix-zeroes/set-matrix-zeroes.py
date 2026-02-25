class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        Row = len(matrix)
        Col = len(matrix[0])

        columns = [1 for _ in range(Col)]
        rows = [1 for _ in range(Row)]

        for r in range(Row):
            for c in range(Col):
                if matrix[r][c] == 0:
                    columns[c] = 0
                    rows[r] = 0

        for r in range(Row):
            for c in range(Col):
                if columns[c] == 0 or rows[r] == 0:
                    matrix[r][c] = 0

            
        