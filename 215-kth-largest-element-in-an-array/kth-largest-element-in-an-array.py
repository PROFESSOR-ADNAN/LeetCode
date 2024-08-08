class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        for i in range(len(nums)-k+1):
            itm = heapq.heappop(nums)
        return itm