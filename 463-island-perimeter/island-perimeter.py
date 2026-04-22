class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        Row = len(grid)
        Col = len(grid[0])
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(r, c):
            return 0 <= r < Row and 0 <= c < Col

        visited = set()
        perimeter = 0

        def dfs(r, c):
            nonlocal perimeter

            visited.add((r, c))
            for dx, dy in direction:
                newR, newC = r + dx, c + dy
                if not inbound(newR, newC) or grid[newR][newC] == 0:
                    perimeter += 1
                elif (newR, newC) not in visited:
                    dfs(newR, newC)

        for r in range(Row):
            for c in range(Col):
                if grid[r][c] == 1 and (r, c) not in visited:
                    dfs(r, c)

        return perimeter


