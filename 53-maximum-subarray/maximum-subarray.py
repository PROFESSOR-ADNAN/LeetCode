class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Max = nums[0]
        for i in range(len(nums)):
            currNum = nums[i]
            if currNum > Max:
                Max = currNum

        print(Max)
        Max_sum = Max
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum > Max_sum:
                Max_sum = sum
            if sum < 0:
                sum = 0

        return Max_sum