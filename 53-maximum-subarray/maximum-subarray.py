class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # for i in range(1, len(nums)):
        #     nums[i] += nums[i-1]

        # return max(nums)

        # sm = sum(nums)
        # mx_first = max(nums)
        # temp = nums.copy()

        # for i in range(1, len(temp)):
        #     temp[i] += temp[i-1]

        # mx = max(temp)
        # mn = min(0, min(temp))

        # if sm < 0:
        #     return mx_first
        
        # return mx-mn

        # max_sum = float("-inf")
        # for i in range(len(nums)):
        #     curr = 0
        #     for j in range(i, len(nums)):
        #         curr += nums[j]

        #         max_sum = max(max_sum, curr)

        # return max_sum

        max_sum = float("-inf")
        curr = 0

        for i in range(len(nums)):
            curr += nums[i]

            max_sum = max(max_sum, curr)

            if curr < 0:
                curr = 0

        return max_sum


            

        
