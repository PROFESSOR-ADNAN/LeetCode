class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # cookies = [1, 2, 3]
        # k = 4

        # allSplit = []

        # def backtrack(path):
        #     if len(path) == len(cookies):
        #         allSplit.append(path[:])
        #         return

        #     for j in range(len(cookies)):
        #         if cookies[j] in path:
        #             continue

        #         curr = cookies[j]
        #         path.append(curr)

        #         backtrack(path)
                 
        #         path.pop()

        # backtrack([])
        # print(allSplit)
        # return 0

        # min_unfairness = float("inf")
        # dist = [0] * k

        # def backtrack(i):
        #     nonlocal min_unfairness, dist
        #     if i == len(cookies):
        #         min_unfairness = min(min_unfairness, max(dist))
        #         return 

        #     if min_unfairness <= max(dist): return

        #     for j in range(k):
        #         dist[j] += cookies[i]
        #         backtrack(i+1)

        #         dist[j] -= cookies[i]

        # backtrack(0)
        # return min_unfairness

        # min_unfairness = float("inf")
        # dist = [0] * k

        # def backtrack(i, j):
        #     nonlocal min_unfairness, dist
        #     print(dist)
        #     if i == len(cookies):
        #         min_unfairness = min(min_unfairness, max(dist))
        #         return 
        #     if j == k:
        #         return 

        #     dist[j] += cookies[i]
        #     backtrack(i+1, j) 
        #     dist[j] -= cookies[i]

        #     backtrack(i, j+1)
            

        # backtrack(0, 0)
        # return min_unfairness

        min_unfairness = float("inf")
        dist = [0] * k

        def backtrack(i):
            nonlocal dist, min_unfairness
            if i >= len(cookies):
                min_unfairness = min(min_unfairness, max(dist))
                return

            for j in range(k):
                curr = cookies[i]

                if min_unfairness <= curr: return

                dist[j] += curr
                backtrack(i+1)
                dist[j] -= curr

        backtrack(0)
        return min_unfairness











