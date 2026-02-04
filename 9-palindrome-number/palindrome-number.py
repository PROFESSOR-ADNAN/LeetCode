class Solution:
    def isPalindrome(self, x: int) -> bool:
        div = 1
        while div * 10 < x:
            div *= 10
        while x:
            last_digit = x % 10
            first_digit = x // div
            if last_digit != first_digit:
                return False
            x %= div
            x //= 10
            div //= 100
        
        return True

