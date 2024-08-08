class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort()
        while len(stones) > 1:
            last = stones.pop()
            second_to_last = stones.pop()
            if last - second_to_last != 0:
                stones.append(last-second_to_last)
                stones.sort()

        return stones[0] if len(stones) > 0 else 0
        