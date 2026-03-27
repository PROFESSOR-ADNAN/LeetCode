class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x**n

        # memoization = defaultdict(int)
        # def pow(x, n):
        #     if n == 1:
        #         return x
        #     if n == 0:
        #         return 1

        #     half = n // 2
        #     if half in memoization:
        #         res = memoization[half]
        #     else:
        #         res = pow(x, half)
        #     memoization[half] = res
        #     if n % 2:
        #         return x * res * res
        #     else:
        #         return res * res

        # condition = False
        # if n < 0:
        #     condition = True
        #     n *= -1

        # ans = pow(x, n)

        # if condition:
        #     return 1 / ans
        # else: 
        #     return ans

        def helper(x, n):
            if x == 0: return 0
            if n == 1: return x
            if n == 0: return 1

            res = helper(x*x, n//2)
            return x*res if n%2 else res

        ans = helper(x, abs(n))
        return 1/ans if n < 0 else ans

    