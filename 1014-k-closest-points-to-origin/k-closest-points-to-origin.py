class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distance = []
        for x, y in points:
            dis = (x**2) + (y**2)
            distance.append([dis, x, y])
        distance.sort()
        ans = []
        for dis, x, y in distance:
            ans.append([x, y])
        return ans[:k]












        # minHeap = []
        # for x, y in points:
        #     dist = (x ** 2) + (y ** 2)
        #     minHeap.append([dist, x, y])
        # heapq.heapify(minHeap)
        # res = []
        # while k > 0:
        #     dist, x, y = heapq.heappop(minHeap)
        #     res.append([x, y])
        #     k -= 1
        # return res