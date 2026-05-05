class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # indegree = [0] * numCourses
        # graph = defaultdict(list)
        # for u, v in prerequisites:
        #     graph[v].append(u)
        #     indegree[u] += 1

        # white, grey, black = 0, 1, 2

        # color = {course:white for course in range(numCourses)}

        # def dfs(node):
        #     color[node] = grey
        #     for nei in graph[node]:
        #         if color[nei] == grey: return True
        #         if color[nei] == white:
        #             if dfs(nei):
        #                 return True

        #     color[node] = black

        # for i in range(numCourses):
        #     if color[i] == white:
        #         if dfs(i):
        #             return []

        # q = deque(i for i in range(numCourses) if indegree[i] == 0)

        # top_order = []
        # while q:
        #     node = q.popleft()
        #     top_order.append(node)

        #     for nei in graph[node]:
        #         indegree[nei] -= 1
        #         if indegree[nei] == 0:
        #             q.append(nei)

        # return top_order


        # indegree = [0] * numCourses
        # graph = defaultdict(list)
        # for u, v in prerequisites:
        #     graph[v].append(u)
        #     indegree[u] += 1

        # q = deque(i for i in range(numCourses) if indegree[i] == 0)

        # top_order = []
        # while q:
        #     node = q.popleft()
        #     top_order.append(node)

        #     for nei in graph[node]:
        #         indegree[nei] -= 1
        #         if indegree[nei] == 0:
        #             q.append(nei)

        # return top_order if len(top_order) == numCourses else []

        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)

        white, gray, black = 0, 1, 2
        color = {i:white for i in range(numCourses)}

        top_order = []

        def dfs(node):
            nonlocal top_order 

            color[node] = gray
            for nei in graph[node]:
                if color[nei] == gray: return True
                if color[nei] == white: 
                    if dfs(nei):
                        return True

            color[node] = black
            top_order.append(node)

        for i in range(numCourses):
            if color[i] == white:
                if dfs(i):
                    return []

        return top_order[::-1]