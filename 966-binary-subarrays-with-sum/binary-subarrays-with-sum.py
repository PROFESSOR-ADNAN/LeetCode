class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        def func(nums, goal):
            if goal < 0: return 0
            sum, cnt, l = 0, 0, 0
            for r in range(len(nums)):
                sum += nums[r]
                while sum > goal:
                    sum -= nums[l]
                    l += 1
                cnt += (r-l+1)
            
            return cnt
        
        return func(nums, goal) - func(nums, goal-1)

            
















        # l, r = 0, 0
        # sum = 0
        # counter = 0
        # while r < len(nums):
        #     sum += nums[r]
        #     if sum == goal:
        #         counter += 1
        #     while sum > goal:
        #         sum -= nums[l]
        #         l += 1
        #         if sum == goal:
        #             counter += 1

        