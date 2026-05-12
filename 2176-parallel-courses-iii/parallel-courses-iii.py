class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # graph = defaultdict(list)
        # indegree = [0] * (n + 1)
        # for u, v in relations:
        #     graph[u].append(v)
        #     indegree[v] += 1

        # q = deque([i for i in range(1, n+1) if indegree[i] == 0])

        # min_time = 0

        # while q:
        #     n = len(q)
        #     t = 0
        #     for _ in range(n):
        #         curr = q.popleft()
        #         t = max(t, time[curr-1])
        #         for nei in graph[curr]:
        #             indegree[nei] -= 1
        #             if indegree[nei] == 0:
        #                 q.append(nei)

        #     min_time += t

        # return min_time

        graph = defaultdict(list)
        indegree = [0] * (n + 1)
        for u, v in relations:
            graph[u].append(v)
            indegree[v] += 1

        q = deque([i for i in range(1, n+1) if indegree[i] == 0])

        compeletion_time = {i: time[i-1] for i in q}

        min_time = 0

        while q:
            curr = q.popleft()
            min_time = max(min_time, compeletion_time[curr])
            
            for nei in graph[curr]:
                nei_compelete = compeletion_time.get(nei, 0)
                compeletion_time[nei] = max(nei_compelete, compeletion_time[curr] + time[nei-1])

                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return min_time