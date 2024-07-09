class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max = nums[0]
        max_sofar = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i] + curr_max:
                curr_max = nums[i]
            else:
                curr_max = curr_max + nums[i]
            
            if curr_max > max_sofar:
                max_sofar = curr_max

        return max_sofar