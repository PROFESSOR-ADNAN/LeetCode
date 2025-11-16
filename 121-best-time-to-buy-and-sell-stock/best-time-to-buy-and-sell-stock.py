class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 0
        max_profit = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            max_profit = max(max_profit, prices[r]-prices[l])
            r += 1

        return max_profit




        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if (prices[j]-prices[i]) > max_profit:
        #             max_profit = prices[j] - prices[i]

        # return max_profit
        