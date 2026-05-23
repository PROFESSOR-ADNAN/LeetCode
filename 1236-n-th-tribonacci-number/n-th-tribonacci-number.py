class Solution:
    def tribonacci(self, n: int) -> int:

        # memo = [-1] *(n+1)
        # def helper(n):
        #     nonlocal memo

        #     if n == 0: return 0
        #     if n == 1 or n == 2: return 1
            
        #     if memo[n-1] != -1:
        #         a = memo[n-1]
        #     else:
        #         a = memo[n-1] = helper(n-1)
            
        #     if memo[n-2] != -1:
        #         b = memo[n-2]
        #     else:
        #         b = memo[n-2] = helper(n-2)

        #     if memo[n-3] != -1:
        #         c = memo[n-3]
        #     else:
        #         c = memo[n-3] = helper(n-3)


        #     return a + b + c

        # return helper(n)


        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        tribonacci = [0, 1, 1]
        for i in range(3, n+1):
            sm = tribonacci[i-1] + tribonacci[i-2] + tribonacci[i-3]
            tribonacci.append(sm)

        return tribonacci[-1]