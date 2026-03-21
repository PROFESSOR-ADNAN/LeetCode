class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operation = 0
        for i in range(n-2):
            if nums[i] == 0:
                nums[i] = 1
                operation += 1
                for j in range(i+1, i+3):
                    if nums[j] == 0:
                        nums[j] = 1
                    else:
                        nums[j] = 0

        if sum(nums) == len(nums):
            return operation
        else:
            return -1