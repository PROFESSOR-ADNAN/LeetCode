class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # def index_inbound(r, c):
        #     return 0 <= r < rows and 0 <= c < cols

        # curr_row = rStart
        # curr_col = cStart
        # ans = []
        # direction = "right"
        # step = 2
        # ans.append([curr_row, curr_col])

        # while len(ans) < rows*cols:
        #     if direction == "right":
        #         for i in range(1, step):
        #             curr_col += 1
        #             if index_inbound(curr_row, curr_col):
        #                 ans.append([curr_row, curr_col])
                        
        #         direction = "down"
        #     elif direction == "down":
        #         for i in range(1, step):
        #             curr_row += 1
        #             if index_inbound(curr_row, curr_col):
        #                 ans.append([curr_row, curr_col])
                    
        #         step += 1
        #         direction = "left"

        #     elif direction == "left":
        #         for i in range(1, step):
        #             curr_col -= 1
        #             if index_inbound(curr_row, curr_col):
        #                 ans.append([curr_row, curr_col])
        
        #         direction = "up"

        #     else:
        #         for i in range(1, step):
        #             curr_row -= 1
        #             if index_inbound(curr_row, curr_col):
        #                 ans.append([curr_row, curr_col])
        
        #         step += 1
        #         direction = "right"

        # return ans


        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        ans = []
        step = 1
        ind = 0
        curr_row = rStart
        curr_col = cStart

        while len(ans) < rows * cols:
            for _ in range(2):
                for _ in range(step):
                    if (0 <= curr_row < rows and 0 <= curr_col < cols):
                        ans.append([curr_row, curr_col])
                    r, c = direction[ind]
                    curr_row += r
                    curr_col += c

                ind = (ind + 1) % 4

            step += 1
                    
        return ans