class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum = nums[0]
        max_sum = curr_sum
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], nums[i]+curr_sum)
            max_sum = max(max_sum, curr_sum)

        return max_sum










        # curr_max = nums[0]
        # max_sofar = nums[0]

        # for i in range(1, len(nums)):
        #     if nums[i] > nums[i] + curr_max:
        #         curr_max = nums[i]
        #     else:
        #         curr_max = curr_max + nums[i]
            
        #     if curr_max > max_sofar:
        #         max_sofar = curr_max

        # return max_sofar