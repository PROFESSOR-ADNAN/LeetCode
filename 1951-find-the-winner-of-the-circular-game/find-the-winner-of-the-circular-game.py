class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        q = deque()
        for i in range(1, n+1):
            q.append(i)

        while len(q) > 1:
            for _ in range(k-1):
                num = q.popleft()
                q.append(num)
            q.popleft()

        return q[0]


        # players = list(range(1, n+1))
        # ind = 0

        # while len(players) > 1:
        #     ind = (ind + k - 1) % len(players)
        #     players.pop(ind)
        
        # return players[0]
                