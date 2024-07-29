class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        total = 0
        piles.sort()
        my_ind = len(piles) - 2
        for i in range(len(piles) // 3):
            total += piles[my_ind]
            my_ind -= 2
        return total