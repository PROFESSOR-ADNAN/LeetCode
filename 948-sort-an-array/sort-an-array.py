class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        heapq.heapify(nums)
        ans = []
        for i in range(len(nums)):
            ans.append(heapq.heappop(nums))
        return ans

        

        

        