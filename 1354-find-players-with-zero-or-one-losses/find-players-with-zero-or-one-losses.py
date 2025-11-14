class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        zero_lose = set()
        one_lose = set()
        more_loses = set()

        for winner, loser in matches:
            if winner not in one_lose and winner not in more_loses:
                zero_lose.add(winner)

            if loser in zero_lose:
                zero_lose.remove(loser)
                one_lose.add(loser)
            elif loser in one_lose:
                one_lose.remove(loser)
                more_loses.add(loser)
            elif loser in more_loses:
                continue
            else:
                one_lose.add(loser)
        
        return [sorted(list(zero_lose)), sorted(list(one_lose))]



        # winners = set(val[0] for val in matches)
        # losers = list(val[1] for val in matches)
        # losers.sort()
        # answer = [sorted([val for val in winners if val not in losers]), [val for val in losers if losers.count(val) == 1]]
        # return answer