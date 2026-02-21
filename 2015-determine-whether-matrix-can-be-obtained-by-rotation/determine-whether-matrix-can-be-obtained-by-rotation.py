class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # Row = len(mat)
        # Col = len(mat[0])

        # mat_sum = 0
        # target_sum = 0
        # for r in range(Row):
        #     for c in range(Col):
        #         mat_sum += mat[r][c]
        #         target_sum += target[r][c]

        # return mat_sum == target_sum

        Row = len(mat)
        Col = len(mat[0])

        def rotate_matrix(matrix):
            temp = [[0 for _ in range(Row)] for _ in range(Col)]
            for r in range(Row):
                for c in range(Col):
                    temp[r][c] = matrix[c][r]
            for r in range(Row):
                left, right = 0, Col-1
                while left < right:
                    temp[r][left], temp[r][right] = temp[r][right], temp[r][left]
                    left += 1
                    right -= 1
            return temp

        for _ in range(4):
            target = rotate_matrix(target)
            if target == mat:
                return True

        return False
            

