class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        l = k-1
        r = len(cardPoints) - 1
        temp_sum = sum(cardPoints[:k])
        max_sum = temp_sum
        while k > 0:
            temp_sum -= cardPoints[l]
            l -= 1
            temp_sum += cardPoints[r]
            r -= 1
            print("temp: ", temp_sum)
            max_sum = max(max_sum, temp_sum)
            print(max_sum)
            k -= 1
        return max_sum
        