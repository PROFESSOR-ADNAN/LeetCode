class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        counter = 0
        ind = 0
        while ind < len(costs) and coins - costs[ind] >= 0:
                counter += 1
                coins = coins - costs[ind]
                ind += 1
        return counter