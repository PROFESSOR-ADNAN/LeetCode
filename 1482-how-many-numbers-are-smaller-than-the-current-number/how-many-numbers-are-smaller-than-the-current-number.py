class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        indexed_nums = [(nums[i], i) for i in range(len(nums))]
        indexed_nums.sort()
        print(indexed_nums)
        for i in range(len(indexed_nums)):
            if i > 0 and indexed_nums[i-1][0] == indexed_nums[i][0]:
                nums[indexed_nums[i][1]] = nums[indexed_nums[i-1][1]]
            else:
                nums[indexed_nums[i][1]] = i
        return nums