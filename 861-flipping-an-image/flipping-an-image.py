class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        Row = len(image)
        Col = len(image[0])

        for r in range(Row):
            left, right = 0, Col-1
            while left < right:
                image[r][left], image[r][right] = image[r][right], image[r][left]
                left += 1
                right -= 1
        
        for r in range(Row):
            for c in range(Col):
                if image[r][c] == 0:
                    image[r][c] = 1
                else:
                    image[r][c] = 0

        return image