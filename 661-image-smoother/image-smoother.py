class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        def average_calculator(row, col):
            total_sum = 0
            count = 0
            for r in range(row-1, row+2):
                for c in range(col-1, col+2):
                
                    if r < 0 or r >= R or c < 0 or c >= C:
                        continue
                    count += 1

                    total_sum += img[r][c]

            return total_sum // count

            
        R = len(img)
        C = len(img[0])

        ans_matrix = [[0 for _ in range(C)] for _ in range(R)]

        for row in range(R):
            for col in range(C):
                ans_matrix[row][col] = average_calculator(row, col)
                
        return ans_matrix