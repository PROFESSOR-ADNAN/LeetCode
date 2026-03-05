class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             product *= nums[j]
                
        #     ans.append(product)

        # return ans

        # [1, 2, 3, 4]

        # [1, 1, 2,  6, 24] # prefix[i]
        #   [24, 24, 12, 4, 1] # suffix[i+1]

        # [24, 12, 8, 6]

        n = len(nums)

        prefix = [1]
        for i in range(n):
            prefix.append(prefix[i] * nums[i])

        suffix = [1] * (n+1)
        for i in range(n-1, -1, -1):
            suffix[i] = (suffix[i+1] * nums[i])

        ans = []
        for i in range(n):
            ans.append(prefix[i]*suffix[i+1])

        return ans