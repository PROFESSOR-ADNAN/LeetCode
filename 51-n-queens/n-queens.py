class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Row = n
        # Col = n

        # setRow = set()
        # setCol = set()
        # upDiag = set()
        # downDiag = set()

        # ans = []
        # path = [["."] * Col for _ in range(Row)]

        # def backtrack(r, c):
        #     if r == Row or c == Col:
        #         print("i reached here")
        #         ans.append(path[:])
        #         return
            
        #     for r in range(Row):
        #         for c in range(Col):
        #             if r in setRow or c in setCol or abs(r-c) in upDiag or (r+c) in downDiag:
        #                 continue

        #             path[r][c] = "Q"
        #             setRow.add(r)
        #             setCol.add(c)
        #             upDiag.add(abs(r-c))
        #             downDiag.add(r+c)

        #             print(path)
        #             backtrack(r, c)

        #             path[r][c] = '.'
        #             setRow.remove(r)
        #             setCol.remove(c)
        #             upDiag.remove(abs(r-c))
        #             downDiag.remove(r+c)
                    
        # backtrack(0, 0)
        # return ans

        # setR = set()
        # setC = set()
        # upDiag = set()
        # downDiag = set()

        # ans = []
        # path = [["."] * n for _ in range(n)]

        # def backtrack(i):
        #     if i == n:
        #         ans.append(path)
        #         return

        #     for j in range(n):
        #         if i in setR or j in setC or abs(i-j) in upDiag or (i+j) in downDiag:
        #             continue

        #         path[i][j] = "Q"
        #         setR.add(i)
        #         setC.add(j)
        #         upDiag.add(abs(i-j))
        #         downDiag.add(i+j)

        #         backtrack(i+1)
        #         path[i][j] = "."

        #         setR.remove(i)
        #         setC.remove(j)
        #         upDiag.remove(abs(i-j))
        #         downDiag.remove(i+j)

        # backtrack(0)
        # return ans

    
        result = []
        cols = set()
        diag1 = set()
        diag2 = set()

        # Create board
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                if col in cols or row-col in diag1 or row+col in diag2:
                    continue

                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)

                backtrack(row+1)
                # Backtrack now
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)

        backtrack(0)
        return result