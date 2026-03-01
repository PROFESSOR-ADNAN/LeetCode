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


        Row = len(mat)
        Col = len(mat[0])
        mpp = defaultdict(list)

        for r in range(Row):
            for c in range(Col):
                mpp[r+c].append(mat[r][c])

        turn = 1
        ans = []

        for nums in mpp.values():
            if turn == 0:
                ans.extend(nums)
                turn = 1
            else:
                ans.extend(nums[::-1])
                turn = 0

        return ans