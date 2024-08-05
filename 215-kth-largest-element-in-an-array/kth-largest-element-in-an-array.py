class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        list1 = [-x for x in nums]
        heapq.heapify(list1)
        for i in range(k):
            itm = heapq.heappop(list1)
        return itm * -1
        