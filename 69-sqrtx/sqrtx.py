class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x

        # max_s = 1
        # for i in range(1, x//2+1):
        #     if x >= i*i:
        #         max_s = i
        #     else:
        #         break

        # print(max_s)
        # return int(max_s)

        l = 0
        r = x-1

        max_s = 1
        while l <= r:
            m = (l+r) // 2
            print(m)
            if x >= m*m:
                max_s = m
                l = m + 1
            else:
                r = m - 1

        return int(max_s)