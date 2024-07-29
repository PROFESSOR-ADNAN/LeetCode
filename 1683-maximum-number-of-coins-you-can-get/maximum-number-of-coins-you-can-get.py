class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        total = 0
        piles.sort()
        alice = len(piles) - 1
        me = len(piles) - 2
        my_friend = 0
        while my_friend < me:
            my_coin = piles[me]
            alice -= 2
            me -= 2
            my_friend += 1
            total += my_coin
        return total