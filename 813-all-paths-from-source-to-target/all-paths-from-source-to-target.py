class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        def dfs(node, path):
            path.append(node)
            if node == n - 1:
                ans.append(path[:])
                return

            for nie in graph[node]:
                dfs(nie, path)
                path.pop()

        dfs(0, [])
        return ans



