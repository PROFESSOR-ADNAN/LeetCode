class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort()
        while len(stones) > 1:
            last = len(stones) - 1
            second_to_last = len(stones) - 2
            if stones[last] == stones[second_to_last]:
                stones.pop()
                stones.pop()
            else:
                diff = stones[last] - stones[second_to_last]
                stones.pop()
                stones[second_to_last] = diff
                stones.sort()
        return stones[0] if len(stones) > 0 else 0

        