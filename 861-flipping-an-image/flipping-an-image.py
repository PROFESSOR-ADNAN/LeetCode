class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(image)):
            l = 0
            r = len(image[i]) - 1
            while l <= r:
                image[i][l], image[i][r] = image[i][r], image[i][l]
                l += 1
                r -= 1
        for i in range(len(image)):
            for j in range(len(image)):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image
            