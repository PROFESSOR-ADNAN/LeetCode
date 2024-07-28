class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dis = []
        for i in range(len(points)):
            distance = (((points[i][0]) ** 2) + ((points[i][1]) ** 2)) ** 0.5
            dis.append([distance, points[i]])
        dis.sort()
        result = []
        for i in range(k):
            result.append(dis[i][1])
        return result
            