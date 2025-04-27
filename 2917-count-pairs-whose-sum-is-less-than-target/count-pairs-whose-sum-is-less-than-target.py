class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        count = 0
        l, r = 0, len(nums)-1
        while l < r:
            s = nums[l] + nums[r]
            if s < target:
                count += (r-l)
                l += 1
            else:
                r -= 1

        return count




        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] < target:
        #             count += 1
        
        # return count