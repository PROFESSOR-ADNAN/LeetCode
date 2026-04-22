class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(vertex, visited):
            if vertex == destination:
                return True
            
            visited.add(vertex)
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    if dfs(neighbour, visited):
                        return True

            return False


        return dfs(source, set())