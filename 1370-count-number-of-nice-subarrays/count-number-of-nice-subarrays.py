class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mpp = {0: 1}
        cnt = 0
        prefix_sum = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                prefix_sum += 1
            remove = prefix_sum - k
            if remove in mpp:
                cnt += mpp[remove]
            mpp[prefix_sum] = 1 + mpp.get(prefix_sum, 0)

        return cnt    