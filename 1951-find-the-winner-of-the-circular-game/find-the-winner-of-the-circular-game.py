class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        players = [i for i in range(1, n+1)]

        index = 0
        while len(players) > 1:
            index = (index + k - 1) % len(players)
            players.pop(index)
        
        return players[0]









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
                