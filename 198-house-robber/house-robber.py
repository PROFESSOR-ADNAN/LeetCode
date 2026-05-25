class Solution:
    def rob(self, nums: List[int]) -> int:
        # odd, even = 0, 0
        # for i in range(0, len(nums), 2):
        #     odd += nums[i]
        #     if i+1 < len(nums):
        #         even += nums[i+1]

        # return max(odd, even)

        # mx = 0
        # total = 0
        # def backtrack(i):
        #     nonlocal total, mx
        #     if i >= len(nums):
        #         mx = max(mx, total)
        #         return 

        #     for j in range(i+2, len(nums)+2):
        #         if j >= len(nums): 
        #             backtrack(j)
        #             break

        #         total += nums[j]
        #         backtrack(j)
        #         total -= nums[j]

        # backtrack(-2)
        # return mx

        # def rob(nums):
        #     if not nums: return 0
        #     if len(nums) == 1: return nums[0]

        #     return max(nums[0] + rob(nums[2:]), rob(nums[1:]))

        # return rob(nums)

        if len(nums) == 1: return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]


