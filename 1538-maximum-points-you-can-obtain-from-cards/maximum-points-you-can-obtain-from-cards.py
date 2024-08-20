class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        l, r = 0, len(cardPoints)-k
        total = sum(cardPoints[r:])
        res = total

        while r < len(cardPoints):
            total += (cardPoints[l] - cardPoints[r])
            res = max(res, total)
            l += 1
            r += 1

        return res

        