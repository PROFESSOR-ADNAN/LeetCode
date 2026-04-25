class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Row = len(grid)
        # Col = len(grid[0])
        # direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # def inboundAndValid(r, c):
        #     return 0 <= r < Row and 0 <= c < Col and grid[r][c] == "1"

        # visited = set()
        # def dfs(r, c):
        #     visited.add((r, c))
        #     for dx, dy in direction:
        #         newR, newC = r + dx, c + dy
        #         if inboundAndValid(newR, newC) and (newR, newC) not in visited:
        #             dfs(newR, newC)

        # island = 0
        # for r in range(Row):
        #     for c in range(Col):
        #         if grid[r][c] == "1" and (r, c) not in visited:
        #             dfs(r, c)
        #             island += 1
        
        # return island


        Rows = len(grid)
        Cols = len(grid[0]) 

        def inbound(r, c):
            return 0 <= r < Rows and 0 <= c < Cols and grid[r][c] == "1"

        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visited = set()
        def dfs(r, c):
            visited.add((r, c))
            for dx, dy in direction:
                newR, newC = r + dx, c + dy
                if inbound(newR, newC) and (newR, newC) not in visited:
                    dfs(newR, newC)
        
        island = 0
        for r in range(Rows):
            for c in range(Cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    island += 1

        return island