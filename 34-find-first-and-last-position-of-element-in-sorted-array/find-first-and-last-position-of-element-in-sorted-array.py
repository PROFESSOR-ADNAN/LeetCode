class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = [-1, -1]
        for i in range(len(nums)):
            if nums[i] == target:
                if ans[0] == -1:
                    ans[0] = i
                ans[1] = i
        return ans
            