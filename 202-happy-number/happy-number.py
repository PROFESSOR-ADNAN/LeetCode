class Solution:
    def isHappy(self, n: int) -> bool:
        unique_set = set()

        while n != 1:
            temp = 0
            while n:
                last_digit = n % 10
                n //= 10
                temp += last_digit ** 2

            if temp in unique_set:
                return False

            unique_set.add(temp)
            n = temp

        return True