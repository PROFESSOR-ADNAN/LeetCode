class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        arr = [num for num in range(1, n+1)]
        ind = 0
        while len(arr) > 1:
            ind = (ind + k - 1) % len(arr)
            arr.pop(ind)
        return arr[0]


        # arr = [num for num in range(1, n+1)]
        # while len(arr) > 1:
        #     for i in range(k-1):
        #         arr.append(arr.pop(0))
        #     arr.pop(0)
        # return arr[0]







        # q = deque(range(1, n+1))

        # while len(q) > 1:
        #     for _ in range(k-1):
        #         q.append(q.popleft())
        #     q.popleft()

        # return q[0]

        # players = [i for i in range(1, n+1)]

        # index = 0
        # while len(playindexers) > 1:
        #     index = ( + k - 1) % len(players)
        #     players.pop(index)
        
        # return players[0]


        # def helper(n, k):
        #     if n == 1:
        #         return 0
        #     return (helper(n-1, k) + k) % n
        # return helper(n, k) + 1

        # q = deque()
        # for i in range(1, n+1):
        #     q.append(i)

        # while len(q) > 1:
        #     for _ in range(k-1):
        #         num = q.popleft()
        #         q.append(num)
        #     q.popleft()

        # return q[0]


        # players = list(range(1, n+1))
        # ind = 0

        # while len(players) > 1:
        #     ind = (ind + k - 1) % len(players)
        #     players.pop(ind)
        
        # return players[0]
                