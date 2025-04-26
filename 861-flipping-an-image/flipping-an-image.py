class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in image:
            l = 0
            r = len(row)-1
            while l <= r:
                row[l], row[r] = 1 - row[r], 1 - row[l]
                l += 1
                r -= 1
        return image


        # R = len(image)
        # C = len(image[0])
        # for r in range(R):
        #     for c in range(C):
        #         if image[r][c] == 0:
        #             image[r][c] = 1
        #         else:
        #             image[r][c] = 0
        # for r in range(R):
        #     row = image[r]
        #     l, r = 0, C-1
        #     while l < r:
        #         row[l], row[r] = row[r], row[l]
        #         l += 1
        #         r -= 1
        # return image


        # for row in image:
        #     l = 0
        #     r = len(row) - 1
        #     while l <= r:
        #         row[l], row[r] = 1 - row[r], 1 - row[l]
        #         l += 1
        #         r -= 1
        # return image
            