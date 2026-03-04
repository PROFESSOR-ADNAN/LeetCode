class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # for i in range(1, len(nums)):
        #     nums[i] += nums[i-1]

        # flag = False
        # for num in nums:
        #     if num < 0:
        #         flag = True
        #         break

        # if flag:
        #     for i in range(len(nums)):
        #         if nums[i] < 0:
        #             nums[i] = abs(nums[i])
        #         else:
        #             nums[i] = 0
        #     return max(nums) + 1
        # else:
        #     return 1


        min_sum = float("inf")
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            nums[i] = curr_sum

            min_sum = min(min_sum, curr_sum)

        return abs(min_sum) + 1 if min_sum < 0 else 1