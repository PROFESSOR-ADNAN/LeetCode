class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        values = range(len(nums)+1)
        for val in values:
            if val not in nums:
                return val
                