class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # ans = [-1, -1]
        # flag1 = True
        # for i in range(len(nums)):
        #     if flag1 and nums[i] >= target:
        #         ans[0] = i
        #         flag1 = False

        #     if nums[i] == target:
        #         ans[1] = i

        # if ans[0] >= 0 and ans[1] >= 0:
        #     return ans
        # else:
        #     return [-1, -1]

        start = end = -1

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                start = mid
                right = mid-1
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1

        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                end = mid
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1

        if start > -1 and  end > -1:
            return [start, end]

        return [-1, -1]
