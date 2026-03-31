class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        flag1 = True
        for i in range(len(nums)):
            if flag1 and nums[i] >= target:
                ans[0] = i
                flag1 = False

            if nums[i] == target:
                ans[1] = i

        if ans[0] >= 0 and ans[1] >= 0:
            return ans
        else:
            return [-1, -1]