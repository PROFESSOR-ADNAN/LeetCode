class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """ 
        num = x
        div = 1
        while num > 9:
            div *= 10
            num //= 10
        
        while x:
            last_digit = x % 10
            first_digit = x // div

            if first_digit != last_digit:
                return False

            x %= div
            x //= 10
            div //= 100

        return True

            










        # if x < 0: return False

        # div = 1
        # while x >= div * 10:
        #     div *= 10

        # while x:
        #     left = x // div 
        #     right = x % 10
            
        #     if right != left:
        #         return False
            
        #     x = (x % div) // 10
        #     div //= 100
        # return True











        # if x < 0: return False

        # div = 1
        # while x >= 10 * div:
        #     div *= 10
        
        # while x:
        #     right = x % 10
        #     left = x // div

        #     if right != left: return False

        #     x = (x % div) // 10
        #     div /= 100
            
        # return True
            
        