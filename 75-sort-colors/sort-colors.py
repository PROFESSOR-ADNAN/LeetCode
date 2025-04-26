class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] += 1
        
        i = 0
        for color in range(3):
            for _ in range(count[color]):
                nums[i] = color
                i += 1

        return nums


        # count = [0] * 3
        # for num in nums:
        #     count[num] += 1
    
        # for i in range(1, len(count)):
        #     count[i] += count[i-1]
      
        # i = len(nums)-1
        # ans = [0] * len(nums)

        # while i >= 0:
        #     ans[count[nums[i]] - 1] = nums[i]
        #     count[nums[i]] -= 1
        #     i -= 1
        # for i in range(len(nums)):
        #     nums[i] = ans[i]
        # return nums