class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        l, r = 0, 0
        while r < len(nums):
            if nums[r] == 1:
                max_len = max(max_len, r-l+1)
            else:
                l = r + 1
            r += 1

        return max_len
            


        