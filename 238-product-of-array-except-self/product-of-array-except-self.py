class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []

        prefix = 1
        for num in nums:
            output.append(prefix)
            prefix *= num

        prefix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= prefix
            prefix *= nums[i]

        return output

        

        