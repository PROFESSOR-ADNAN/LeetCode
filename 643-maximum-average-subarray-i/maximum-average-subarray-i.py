class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        l = 0
        r = k
        curr_max = sum(nums[:k])
        maximum = curr_max
        while r < len(nums):
            curr_max -= nums[l]
            curr_max += nums[r]
            l += 1
            r += 1
            if curr_max > maximum:
                maximum = curr_max
        return (maximum/(k * 1.0))
