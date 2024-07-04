class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count_map = {}

        for i in range(len(nums)):
            if nums[i] in count_map:
                return True
            else:
                count_map[nums[i]] = 1
        return False