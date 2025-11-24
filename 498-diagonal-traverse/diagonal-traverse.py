class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        Row = len(mat)
        Col = len(mat[0])

        ans = defaultdict(list)
        for r in range(Row):
            for c in range(Col):
                ans[r+c].append(mat[r][c])

        res = []
        for i in range(Row + Col):

            if i % 2:
                res.extend(ans[i])
            else:
                res.extend(ans[i][::-1])

        return res

        