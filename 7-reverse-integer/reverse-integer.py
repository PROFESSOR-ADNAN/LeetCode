class Solution(object):
    def reverse(self, x):
        """
        :type x: int    
        :rtype: int
        """
        Min = -1 * (2 ** 31)
        Max = ((2 ** 31) - 1)
        revNum = 0
        sign = 1

        while x:
            if x < 0:
                sign = -1
            x = abs(x)

            digit = int(x % 10)  
            x = int(x / 10)         
            
            if (revNum > Max / 10 or revNum == Max / 10 and digit > Max % 10):
                return 0
            if (revNum < Min / 10 or revNum == Min / 10 and digit < Min % 10):
                return 0
            
            revNum = revNum *10 + digit

        return sign * revNum