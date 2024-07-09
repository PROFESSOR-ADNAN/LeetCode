class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index += 1
        return index