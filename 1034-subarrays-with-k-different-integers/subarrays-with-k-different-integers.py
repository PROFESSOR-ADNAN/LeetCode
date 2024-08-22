class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def func(k):
            cnt, l = 0, 0
            mpp = {}
            for r in range(len(nums)):
                mpp[nums[r]] = 1 + mpp.get(nums[r], 0)
                while len(mpp) > k:
                    mpp[nums[l]] -= 1
                    if mpp[nums[l]] == 0:
                        del mpp[nums[l]]
                    l += 1
                cnt += (r-l+1)

            return cnt

        return func(k) - func(k-1)