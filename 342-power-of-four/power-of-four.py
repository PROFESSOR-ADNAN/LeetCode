class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 0
        num = 4
        while (num ** x) <= n:
            if (num ** x) == n:
                return True
            x += 1
        
        return False
      
      
      
      
      
      
      
      
      
      
        # if n == 1:
        #     return True
        # if n == 0 or n % 4 != 0:
        #     return False
        # return self.isPowerOfFour(n//4)
