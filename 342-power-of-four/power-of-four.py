class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = 1
        while num <= n:
            if num == n:
                return True
            num *= 4

        if num == n: return True 
        else: return False



        # x = 0
        # num = 4
        # while (num ** x) <= n:
        #     if (num ** x) == n:
        #         return True
        #     x += 1

        # return False
      
      
        # if n == 1:
        #     return True
        # if n == 0 or n % 4 != 0:
        #     return False
        # return self.isPowerOfFour(n//4)
