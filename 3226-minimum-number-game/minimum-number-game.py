class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        nums = sorted(nums)
        for i in range(0, len(nums), 2):
            res.extend(nums[i:i+2][::-1])
        return res