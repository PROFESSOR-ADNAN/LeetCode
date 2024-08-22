class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def func(k):
            
            if k < 0: return 0
            curr, cnt, l = 0, 0, 0
            for r in range(len(nums)):
                if nums[r] % 2 == 1:
                    curr += 1
                while curr > k:
                    if nums[l] % 2 == 1:
                        curr -= 1
                    l += 1
                cnt += (r-l+1)
            
            return cnt

        return func(k) - func(k-1)