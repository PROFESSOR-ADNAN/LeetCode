class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[nums[i]-1] += 1

        res = [-1, -1]
        for i in range(len(nums)):
            if ans[i] == 2:
                res[0] = i+1

            if ans[i] == 0:
                res[1] = i+1

        return res