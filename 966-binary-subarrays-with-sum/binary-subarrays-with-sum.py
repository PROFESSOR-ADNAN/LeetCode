class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # n = len(nums)
        # count = 0
        # for i in range(n):
        #     curr = 0
        #     for j in range(i, n):
        #         curr += nums[j]

        #         if curr ==  goal:
        #             count += 1
        #         elif curr > goal:
        #             break

        # return count

        # n = len(nums)
        # left = 0
        # right = 0
        # curr = 0
        # count = 0

        # while right < n:
        #     curr += nums[right]

        #     while left < right and curr >= goal:
        #         curr -= nums[left]
        #         left += 1
        #         if curr == goal:
        #             count += 1

        #     if curr == goal:
        #         count += 1

        #     right += 1

        # return count

        # def helper(num, nums):
        #     n = len(nums)
        #     left = 0
        #     curr = 0
        #     count = 0

        #     for right in range(n):
        #         curr += nums[right]
                
        #         while left <= right and curr > num:
        #             curr -= nums[left]
        #             left += 1

        #         if curr <= num:
        #             count += right - left + 1

        #     return count

        
        # return helper(goal, nums) - helper(goal-1, nums)


        def helper(nums, k):
            n = len(nums)
            curr = 0
            count = 0

            left = 0
            for right in range(n):
                curr += nums[right]

                while left <= right and curr > k:
                    curr -= nums[left]
                    left += 1
                
                count += right - left

            return count

        return helper(nums, goal) - helper(nums, goal-1)