class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in image:
            l = 0
            r = len(row) - 1
            while l <= r:
                row[l], row[r] = 1 - row[r], 1 - row[l]
                l += 1
                r -= 1
        return image
            