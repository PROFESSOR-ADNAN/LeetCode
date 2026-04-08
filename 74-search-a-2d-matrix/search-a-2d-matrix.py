class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Row = len(matrix)
        Col = len(matrix[0])

        top, bottom = 0, Row - 1
        while top <= bottom:
            mid = top + (bottom - top) // 2
            curr_row = matrix[mid]

            if target > curr_row[-1]:
                top = mid + 1
            elif target < curr_row[0]:
                bottom = mid - 1
            else:
                break

        left, right = 0, Col - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == curr_row[mid]:
                return True
            elif target > curr_row[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return False

