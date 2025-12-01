class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        forward = [0] * len(nums)
        backward = [0] * len(nums)

        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            forward[i] = cur
        
        cur = 0
        for i in range(len(nums)-1, -1, -1):
            cur += nums[i]
            backward[i] = cur

        for i in range(len(nums)):
            if forward[i] == backward[i]:
                return i
        return -1
       
       
       
       
       
       
       
       
       
       
       
       
        # total = sum(nums)
        # left = 0

        # for i, num in enumerate(nums):
        #     total -= num
        #     if total == left:
        #         return i
        #     left += num
        # return -1
        
        # Rprefix = nums[:]

        # for i in range(len(nums)-2, -1, -1):
        #     Rprefix[i] += Rprefix[i+1]

        # for i in range(1, len(nums)):
        #     nums[i] += nums[i-1]

        # for i in range(len(nums)):
        #     if Rprefix[i] == nums[i]:
        #         return i
        # return -1