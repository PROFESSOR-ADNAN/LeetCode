class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        path = []
        ans = []

        def backtrack(cand):
            if len(path) == k:
                ans.append(path[:])
                return

            for i in range(len(cand)):
                path.append(cand[i])
                backtrack(cand[i+1:])
                path.pop()


        backtrack(nums)
        return ans
