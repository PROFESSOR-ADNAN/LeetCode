class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Row = len(mat)
        # Col = len(mat[0])
        
        # ans = []

        # for i in range(1):
        #     ans.append(mat[i][i])

        # for i in range(2):
        #     ans.append(mat[i][1-i])

        # for i in range(3):
        #     ans.append(mat[2-i][i])

        # for i in range(1, 3):
        #     ans.append(mat[i][3-i])

        # for i in range(2, 3):
        #     ans.append(mat[i][i])

        # return ans


        # Row = len(mat)
        # Col = len(mat[0])
        # mpp = defaultdict(list)

        # for r in range(Row):
        #     for c in range(Col):
        #         mpp[r+c].append(mat[r][c])

        # turn = 1
        # ans = []

        # for nums in mpp.values():
        #     if turn == 0:
        #         ans.extend(nums)
        #         turn = 1
        #     else:
        #         ans.extend(nums[::-1])
        #         turn = 0

        # return ans


        Row = len(mat)
        Col = len(mat[0])

        curr_row = curr_col = 0
        direction = True
        ans = []

        while len(ans) < Row * Col:
            if direction:
                while curr_row >= 0 and curr_col < Col:
                    ans.append(mat[curr_row][curr_col])

                    curr_row -= 1
                    curr_col += 1
                
                if curr_col == Col:
                    curr_row += 2
                    curr_col -= 1
                else:
                    curr_row += 1

                direction = False
            else:
                while curr_col >= 0 and curr_row < Row:
                    ans.append(mat[curr_row][curr_col])

                    curr_row += 1
                    curr_col -= 1

                if curr_row == Row:
                    curr_col += 2
                    curr_row -= 1
                else:
                    curr_col += 1

                direction = True

        return ans
