class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        Row = len(grid)
        Col = len(grid[0])

        negative_number = 0
        for r in range(Row):
            for c in range(Col):
                if grid[r][c] < 0:
                    negative_number += 1
        
        return negative_number