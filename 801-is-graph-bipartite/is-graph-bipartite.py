class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colorMap = {}

        def dfs(vertex, color):
            colorMap[vertex] = color
            
            for nei in graph[vertex]:
                if nei in colorMap:
                    if colorMap[nei] == color:
                        return False
                else:
                    if not dfs(nei, not color):
                        return False
            return True

        for i in range(len(graph)):
            if i not in colorMap:
                if not dfs(i, 0):
                    return False

        return True
