class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        Row = len(img)
        Col = len(img[0]) 

        def filter(r, c):
            total = 0
            count = 0

            for row in range(r-1, r+2):
                for col in range(c-1, c+2):
                    if row < 0 or row >= Row or col < 0 or col >= Col:
                        continue
                    total += img[row][col]
                    count += 1
            
            return math.floor(total/count)

        ans = [[0 for i in range(Col)] for _ in range(Row)]

        for r in range(Row):
            for c in range(Col):
                ans[r][c] = filter(r, c)

        return ans

