class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        trailing_zeros = 0
        divisor = 5
        while n >= divisor:
            trailing_zeros += n // divisor
            divisor *= 5

        return trailing_zeros


    #     result = self.factorial(n)
    #     trailing_zeros = 0
    #     while result % 10 == 0:
    #         trailing_zeros += 1
    #         result /= 10
        
    #     return trailing_zeros

    # def factorial(self, n):
    #     if n == 0 or n == 1:
    #         return 1
    #     return n * self.factorial(n-1)