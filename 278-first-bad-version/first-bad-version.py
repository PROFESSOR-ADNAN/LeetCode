# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # left, right = 0, n
        # while left <= right:
        #     mid = (left + right) // 2
        #     if isBadVersion(mid):
        #         right = mid-1
        #     else:
        #         left = mid + 1

        # return left



        low, high = 1, n
        while low <= high:
            mid = low + (high - low) // 2

            if isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low