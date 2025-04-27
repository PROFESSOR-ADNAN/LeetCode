class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []

        for k in range(len(nums)):
            if k and nums[k] == nums[k-1]:
                continue

            l, r = k + 1, len(nums) - 1
            while l < r:
                s = nums[k] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ans.append([nums[k], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-l]: r -= 1
                    l, r = l+1, r-1

        return ans





        # nums.sort()
        # ans = []
 
        # for k in range(len(nums)):
        #     l, r = k + 1, len(nums) - 1
        #     while l < r:
        #         s = nums[k] + nums[l] + nums[r]
        #         if s < 0:
        #             l += 1
        #         elif s > 0:
        #             r -= 1
        #         else:
        #             if [nums[k], nums[l], nums[r]] not in ans:
        #                 ans.append([nums[k], nums[l], nums[r]])
        #             l += 1
        #             r -= 1
        
        # return ans



        # nums.sort()
        # ans = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 if [nums[i], nums[j], nums[k]] not in ans:
        #                     ans.append([nums[i], nums[j], nums[k]])
         
        # return ans