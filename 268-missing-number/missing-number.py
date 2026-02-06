class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        compeleteNums = [i for i in range(len(nums)+1)]

        for num in compeleteNums:
            if num not in nums:
                return num