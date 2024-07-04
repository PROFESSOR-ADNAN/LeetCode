class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1

        while j < len(nums):
            if nums[j] > nums[i]:
                nums[i+1] = nums[j]
                i += 1
                j += 1
            else:
                j += 1
        k = i + 1
        for m in range(i + 1, len(nums)):
            nums[m] = ""
        
        return k
            