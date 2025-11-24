class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        Row = len(matrix)
        Col = len(matrix[0])
        
        for r in range(Row//2):
            for c in range(Col):
                matrix[r][c], matrix[Row-r-1][c] = matrix[Row-r-1][c], matrix[r][c]

        for r in range(Row):
            for c in range(r, Col):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]






        # Row = len(matrix)
        # Col = len(matrix[0])

        # left = 0
        # right = Col-1
        # top = 0
        # bottom = Row-1

        # for r in range((Row*Col)//2):

        #     if left == right:
        #         right -= 1
        #         left = 1
        #     if top == bottom:
        #         bottom -= 1
        #         right = 1

        #     first_val = matrix[top][left]

        #     matrix[top][left] = matrix[bottom][left]
        #     matrix[bottom][left] = matrix[bottom][right]
        #     matrix[bottom][right] = matrix[top][right]
        #     matrix[top][right] = first_val
            
        #     top += 1
        #     left += 1

           

        # print(matrix)
