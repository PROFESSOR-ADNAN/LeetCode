class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ind = 0
        for search in range(len(nums)):
            if nums[search] != 0:
                nums[search], nums[ind] = nums[ind], nums[search]
                ind += 1
       
       
       
       
       
       
       
       
       
       
       
       
       
        # ind = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[i], nums[ind] = nums[ind], nums[i]
        #         ind += 1


        # return nums


        
        
        
        # i, j = 0, 0
        # while j < len(nums):
        #     if nums[j] != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 1
        #     j += 1

        # return nums
        