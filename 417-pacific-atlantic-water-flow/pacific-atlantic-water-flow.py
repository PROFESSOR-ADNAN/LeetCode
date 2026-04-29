class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Rows = len(heights)
        # Cols = len(heights[0])

        # direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # def inbound(r, c):
        #     return 0 <= r < Rows and 0 <= c < Cols

        # pacfic = set()
        # atlantic = set()

        # def dfsPacfic(r, c):
        #     if r == 0 or c == 0:
        #         return True

        #     for dx, dy in direction:
        #         newR, newC = r + dx, c + dy
        #         if (newR == Rows or newC == Cols) or heights[r][c] < heights[newR][newC]:
        #             return False
        #         else:
        #             dfsPacfic(newR, newC)

        # def dfsAtlantic(r, c):
        #     if r == Rows - 1 or c == Cols - 1:
        #         return True

        #     for dx, dy in direction:
        #         newR, newC = r + dx, c + dy
        #         if (newR == -1 or newC == -1) or heights[r][c] < heights[newR][newC]:
        #             return False
        #         else:
        #             dfsAtlantic(newR, newC)

        # for r in range(Rows):
        #     for c in range(Cols):
        #         if dfsPacfic(r, c):
        #             pacfic.add((r, c))
        #         if dfsAtlantic(r, c):
        #             atlantic.add((r, c))
        # print(sorted(list(pacfic)))
        # print(atlantic)

        # ans = []
        # for r in range(Rows):
        #     for c in range(Cols):
        #         if (r, c) in pacfic and (r, c) in atlantic:
        #             ans.append((r, c))

        # return ans

        Rows = len(heights)
        Cols = len(heights[0])

        pac = set()
        atl = set()

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def inbound(r, c, prevHeight):
            return 0 <= r < Rows and 0 <= c < Cols and heights[r][c] >= prevHeight

        def dfs(r, c, dest, prevHeight):
            dest.add((r, c))

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if inbound(nr, nc, heights[r][c]) and (nr, nc) not in dest:
                    dfs(nr, nc, dest, heights[nr][nc])

        for c in range(Cols):
            dfs(0, c, pac, heights[0][c])
            dfs(Rows-1, c, atl, heights[Rows-1][c])


        for r in range(Rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, Cols-1, atl, heights[r][Cols-1])

        ans = []
        for r in range(Rows):
            for c in range(Cols):
                if (r, c) in pac and (r, c) in atl:
                    ans.append((r, c))

        return ans

            

        

