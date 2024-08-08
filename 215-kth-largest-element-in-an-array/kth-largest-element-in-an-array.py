class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for i in range(k):
            kth_largest = heapq.heappop(nums)
        return kth_largest * -1
        