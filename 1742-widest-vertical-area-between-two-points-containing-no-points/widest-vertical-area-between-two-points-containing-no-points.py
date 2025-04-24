class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        max_diff = 0
        for i in range(1, len(points)):
            x1 = points[i-1][0]
            x2 = points[i][0]
            max_diff = max(max_diff, x2-x1)
        
        return max_diff
        