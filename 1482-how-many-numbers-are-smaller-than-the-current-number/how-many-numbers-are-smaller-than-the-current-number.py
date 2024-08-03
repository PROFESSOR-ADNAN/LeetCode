class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        max_value = max(nums) 
        min_value = min(nums)
        range_value = max_value - min_value + 1

        count = [0] * range_value
        for num in nums:
            count[num-min_value] += 1

        for i in range(1, len(count)):
            count[i] += count[i-1]

        for i in range(len(nums)):
            if nums[i] == min_value:
                nums[i] = 0
            else:
                nums[i] = count[nums[i] - min_value - 1]
        return nums