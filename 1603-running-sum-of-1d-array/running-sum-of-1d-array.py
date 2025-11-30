class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
       
       
       
        # for i in range(1, len(nums)):
        #     nums[i] += nums[i-1]
        # return nums





        # sum = 0
        # res = []
        # for i in range(len(nums)):
        #     sum += nums[i]
        #     res.append(sum)
        # return res