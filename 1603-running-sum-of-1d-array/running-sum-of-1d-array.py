class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        res = []
        for i in range(len(nums)):
            sum += nums[i]
            res.append(sum)
        return res