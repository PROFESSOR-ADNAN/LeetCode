class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # ans = [0] * len(nums)
        # for i in range(len(nums)):
        #     ans[nums[i]-1] += 1

        # res = [-1, -1]
        # for i in range(len(nums)):
        #     if ans[i] == 2:
        #         res[0] = i+1

        #     if ans[i] == 0:
        #         res[1] = i+1

        # return res    

        ans = [0, 0]

        for num in nums:
            num = abs(num)
            if nums[num-1] < 0:
                ans[0] = num
            nums[num-1] = -nums[num-1]

        for ind, num in enumerate(nums):
            if num > 0 and ind + 1 != ans[0]:
                ans[1] = ind + 1
                return ans
