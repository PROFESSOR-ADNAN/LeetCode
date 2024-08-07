class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        heapq.heapify(nums)
        res =  []
        for i in range(len(nums)):
            res.append(heapq.heappop(nums))
        return res
        

        

        

        