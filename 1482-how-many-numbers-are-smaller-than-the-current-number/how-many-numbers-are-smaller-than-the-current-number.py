class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        count = 0
        for i in range(len(nums)):
            current_element = nums[i]
            for j in range(len(nums)):
                if nums[j] < current_element:
                    count += 1
            result.append(count)
            count = 0
        return result