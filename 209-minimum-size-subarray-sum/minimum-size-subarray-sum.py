class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, 0
        sum_ = 0
        minLen = float("inf")

        while r < len(nums):
            sum_ += nums[r]

            while sum_ >= target:
                minLen = min(minLen, r-l+1)
                sum_ -= nums[l]
                l += 1
            r += 1

        return minLen if minLen != float("inf") else 0