class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        mpp = {0: 1}
        cnt = 0
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            remove = prefix_sum - goal
            if remove in mpp:
                cnt += mpp[remove]
            mpp[prefix_sum] = 1 + mpp.get(prefix_sum, 0)
        
        return cnt
















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

        