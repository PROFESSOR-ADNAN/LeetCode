class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        trailing_zeros = 0
        divisor = 5

        while n >= divisor:
            trailing_zeros += (n // divisor)
            divisor *= 5

        return trailing_zeros


        # def factorial(n):
        #     if n == 1 or n == 0:
        #         return 1
        #     return n * factorial(n-1)

        # n_factorial = factorial(n)

        # trailing_zeros = 0
        # while n_factorial:
        #     last_digit = n_factorial % 10
        #     if last_digit == 0:
        #         trailing_zeros += 1
        #     else:
        #         break
        #     n_factorial /= 10

        # return trailing_zeros


        # trailing_zeros = 0
        # divisor = 5
        # while n >= divisor:
        #     trailing_zeros += n // divisor
        #     divisor *= 5

        # return trailing_zeros


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