class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        l, r = -1, num
        while l <= r:
            mid = l + (r-l) // 2
            val = mid * 3
            if val == num:
                return [mid-1, mid, mid+1]
            elif val > num:
                r = mid-1
            else:
                l = mid+1
        return []