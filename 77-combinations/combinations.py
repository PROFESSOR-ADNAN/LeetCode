class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # nums = [i for i in range(1, n+1)]
        # path = []
        # ans = []

        # def backtrack(cand):
        #     if len(path) == k:
        #         ans.append(path[:])
        #         return

        #     for i in range(len(cand)):
        #         path.append(cand[i])
        #         backtrack(cand[i+1:])
        #         path.pop()


        # backtrack(nums)
        # return ans

        ans = []
        comb = []

        def backtrack(start):
            if len(comb) == k:
                ans.append(comb[:])
                return

            for num in range(start, n+1):
                comb.append(num)
                backtrack(num+1)
                comb.pop()

        backtrack(1)
        return ans
