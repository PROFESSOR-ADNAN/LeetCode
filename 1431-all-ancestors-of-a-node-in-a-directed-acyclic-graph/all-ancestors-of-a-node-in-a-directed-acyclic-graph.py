class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # graph = defaultdict(list)
        # for u, v in edges:
        #     graph[u].append(v)

        # def dfs(i, val):
        #     for nei in graph[i]:
        #         ans[nei].add(val)
        #         dfs(nei, val)

        # ans = []
        # for i in range(n):
        #     ans.append(set())

        # for i in range(n):
        #     val = i
        #     dfs(i, val)

        # for i in range(n):
        #     ans[i] = sorted(list(ans[i]))

        # return ans

        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        q = deque([i for i in range(n) if indegree[i] == 0])

        ancestors = defaultdict(set)
        while q:
            curr = q.popleft()
            for nei in graph[curr]:
                ancestors[nei].update(ancestors[curr])
                ancestors[nei].add(curr)
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        ans = []
        for i in range(n):
            ans.append(sorted(list(ancestors[i])))

        return ans