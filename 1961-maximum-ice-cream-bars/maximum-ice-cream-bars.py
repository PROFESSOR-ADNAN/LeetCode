class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        ans = 0
        ind = 0
        # print(costs)
        while coins:
            if ind < len(costs) and coins >= costs[ind]:
                ans += 1
                coins -= costs[ind]
                ind += 1
            else:
                break
        return ans

















        # costs.sort()
        # res = 0
        # ind = 0
        # while ind < len(costs) and coins >= costs[ind]:
        #     coins -= costs[ind]
        #     ind += 1
        #     res += 1
        # return res