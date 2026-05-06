class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
        reversedGraph = defaultdict(list)
        for u in range(n):
            for v in graph[u]:
                reversedGraph[v].append(u)
                indegree[u] += 1
        
        safe = []
        q = deque([i for i in range(n) if indegree[i] == 0])

        while q:
            curr = q.popleft()
            safe.append(curr)

            for nei in reversedGraph[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return sorted(safe)