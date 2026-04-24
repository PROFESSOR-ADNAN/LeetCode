class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Row = len(board)
        # Col = len(board[0])

        # direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # def inboundAndValid(r, c):
        #     return 0 <= r < Row and 0 <= c < Col and board[r][c] == "O"

        # visited = set()

        # def dfs(r, c):
        #     visited.add((r, c))
        #     curr.append((r, c))
        #     for dx, dy in direction:
        #         newR, newC = r + dx, c + dy
        #         if inboundAndValid(newR, newC):
                    


        # for r in range(Row):
        #     for c in range(Col):
        #         curr = []
        #         if board[r][c] == "O" and (r, c) not in visited:
        #             if dfs(r, c):
        #                 for row, col in curr:
        #                     board[row][col] = "X"

        # Row = len(board)
        # Col = len(board[0])

        # direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # def isNotEdge(r, c):
        #     return 1 <= r < Row-1 and 1 <= c < Col-1

        # def capture(arr):
        #     for r, c in arr:
        #         board[r][c] = "X"

        # visited = set()

        # def dfs(r, c):
        #     visited.add((r, c))
        #     curr.append((r, c))

        #     for dx, dy in direction:
        #         newR, newC = r + dx, c + dy
        #         if not isNotEdge(newR, newC):
        #             return False
        #         if board[newR][newC] == "O" and (newR, newC) not in visited:
        #             if not dfs(newR, newC):
        #                 return False

        #     return True


        # for r in range(Row):
        #     for c in range(Col):
        #         curr = []
        #         if isNotEdge(r, c) and (r, c) not in visited and board[r][c] == "O":
        #             if dfs(r, c):
        #                 capture(curr)

        Rows = len(board)
        Cols = len(board[0])

        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def isValid(r, c):
            return 0 <= r < Rows and 0 <= c < Cols and board[r][c] == "O"

        def dfs(r, c):
            if not isValid(r, c):
                return

            board[r][c] = "T"

            for dx, dy in direction:
                newR, newC = r + dx, c + dy
                dfs(newR, newC)


        for r in range(Rows):
            for c in range(Cols):
                if (board[r][c] == "O" and (r in [0, Rows - 1] or c in [0, Cols - 1])):
                    dfs(r, c)

        for r in range(Rows):
            for c in range(Cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(Rows):
            for c in range(Cols):
                if board[r][c] == "T":
                    board[r][c] = "O"