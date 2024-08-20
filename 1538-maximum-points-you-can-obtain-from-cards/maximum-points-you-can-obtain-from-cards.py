class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        window_sum = sum(cardPoints[:k])
        max_sum = window_sum
        l = k-1
        r = len(cardPoints)-1
        while l >= 0:
            window_sum -= cardPoints[l]
            l -= 1
            window_sum += cardPoints[r]
            r -= 1

            max_sum = max(max_sum, window_sum)

        return max_sum

        