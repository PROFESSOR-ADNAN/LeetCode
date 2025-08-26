class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        maxDiagonal = 0
        maxArea = 0
        for l, w in dimensions:
            diagonal = ((l*l) + (w*w))
            area = l * w
            if diagonal > maxDiagonal:
                maxDiagonal = diagonal
                maxArea = area
            if diagonal == maxDiagonal:
                maxArea = max(maxArea, area)

        return maxArea
            