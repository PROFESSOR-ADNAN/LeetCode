class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        l, r = k-1, len(cardPoints)-1
        total = sum(cardPoints[:k])
        res = total

        while l >= 0:
            total += (cardPoints[r] - cardPoints[l])
            res = max(res, total)
            l -= 1
            r -= 1

        return res


        