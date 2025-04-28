class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, 0
        curr = 0
        minLen = float('inf')
        while r < len(nums):
            curr += nums[r]
            while curr >= target:
                if (r-l+1) < minLen:
                    minLen = r-l+1
                curr -= nums[l]
                l += 1
            r += 1
        
        return minLen if minLen != float('inf') else 0



        # minLen = float('inf')
        # for i in range(len(nums)):
        #     curr = 0
        #     for j in range(i, len(nums)):
        #         curr += nums[j]
        #         if curr >= target:
        #             if (j-i+1) < minLen:
        #                 minLen = j-i+1
        #                 break
        
        # return minLen if minLen != float('inf') else 0









        # start = 0
        # sum = 0
        # end = 0
        # result = len(nums)
        # while end < len(nums):
        #     sum += nums[end]
        #     end += 1
        #     while sum >= target:
        #         result = min(result, end - start)
        #         sum -= nums[start]
        #         start += 1
        # return result
        