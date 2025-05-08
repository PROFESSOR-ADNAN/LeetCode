class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_left = []
        prefix_right = [0] * len(nums)

        temp = 0
        for num in nums:
            temp += num
            prefix_left.append(temp)

        temp = 0
        for i in range(len(nums)-1, -1, -1):
            temp += nums[i]
            prefix_right[i] = temp

        for i in range(len(nums)):
            if prefix_left[i] == prefix_right[i]:
                return i
        return -1