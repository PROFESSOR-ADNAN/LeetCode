class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ind = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ind] = nums[i]
                ind += 1
        return ind











        # index = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[index] = nums[i]
        #         index += 1
        # return index