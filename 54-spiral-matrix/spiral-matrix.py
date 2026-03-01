class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Row = len(matrix)
        # Col = len(matrix[0])

        # ans = []

        # top = left = 0
        # bottom = Row - 1
        # right = Col - 1

        # while left <= right and top <= bottom:
        #     for c in range(left, right+1):
        #         ans.append(matrix[top][c])
        #     top += 1

        #     for r in range(top, bottom+1):
        #         ans.append(matrix[r][right])
        #     right -= 1

        #     for c in range(right, left-1, -1):
        #         ans.append(matrix[bottom][c])
        #     bottom -= 1

        #     for r in range(bottom, top-1, -1):
        #         ans.append(matrix[r][left])
        #     left += 1


        #     print(ans)
        #     print(top, bottom)
        #     print(left, right)
        

        # return []


        Row = len(matrix)
        Col = len(matrix[0])

        ans = []

        left, right = 0, Col
        top, bottom = 0, Row

        while left < right and top < bottom:
            # get the elements on the top row
            for col in range(left, right):
                ans.append(matrix[top][col])
            top += 1

            # get the elements on the right column
            for row in range(top, bottom):
                ans.append(matrix[row][right-1])
            right -= 1

            if not(left < right and top < bottom):
                break

            # get the elements on the bottom Row
            for col in range(right-1, left-1, -1):
                ans.append(matrix[bottom-1][col])
            bottom -= 1

            # get the elements on the left column
            for row in range(bottom-1, top-1, -1):
                ans.append(matrix[row][left])
            left += 1

        return ans