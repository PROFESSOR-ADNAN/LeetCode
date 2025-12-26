class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n % 4 != 0 or n < 1:
            return False
        return self.isPowerOfFour(n/4)


        # def power_of_4(n):
        #     if n == 1:
        #         return True
        #     if n < 1:
        #         return False
        #     return power_of_4(n/4)

        # return power_of_4(n)