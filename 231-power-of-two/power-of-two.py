class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        pow = 0
        while (2 ** pow) <= n:
            if n == (2 ** pow):
                return True
            pow += 1
        return False