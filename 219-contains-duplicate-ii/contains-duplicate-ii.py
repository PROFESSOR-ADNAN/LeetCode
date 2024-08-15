class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = set()
        l, r = 0, 0
        while r < len(nums):
            if nums[r] in seen:
                return True
            else:
                seen.add(nums[r])
            if len(seen) == k+1:
                seen.remove(nums[l])
                l += 1
            r += 1

        return False