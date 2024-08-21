class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        max_len = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                l = r+1
            max_len = max(max_len, r-l+1)
        
        return max_len
        
            


        