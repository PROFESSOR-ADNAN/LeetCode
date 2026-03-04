class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        print(nums)
        flag = False
        for num in nums:
            if num < 0:
                flag = True
                break

        if flag:
            for i in range(len(nums)):
                if nums[i] < 0:
                    nums[i] = abs(nums[i])
                else:
                    nums[i] = 0
            return max(nums) + 1
        else:
            return 1
