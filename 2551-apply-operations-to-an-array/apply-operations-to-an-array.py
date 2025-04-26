class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                nums[i-1] *= 2
                nums[i] = 0
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return nums











        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i+1]:
        #         nums[i] = nums[i] * 2
        #         nums[i+1] = 0
        # l = 0
        # r = len(nums) - 1
        # while l < r:
        #     while l < r and nums[l] != 0:
        #         l += 1
        #     while l < r and nums[r] == 0:                      
        #         r -= 1
        #     nums[l], nums[r] = nums[r], nums[l]
        # return nums
        