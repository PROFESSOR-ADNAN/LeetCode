class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        """
        let p1 = (x1, y1), p2 = (x2, y2)
        distance between two points = (x2-x1)**2 + (y2-y1)**2 under root
        let p1 = (1, 2), p2 = (2, 3)
        distance between two points = (1)**2 + (1)**2 = root(2)
        """
        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n):
            x1, y1, r = bombs[i]
            for j in range(n):
                if i == j: continue
                x2, y2, _ = bombs[j]

                distance = (((x2-x1)**2) + ((y2-y1)**2)) ** 0.5
                if distance <= r:
                    graph[i].append(j)

        def dfs(node, visited):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei, visited)

        longest = 0
        for i in range(n):
            visited = set()
            dfs(i, visited)
            longest = max(longest, len(visited))

        return longest



