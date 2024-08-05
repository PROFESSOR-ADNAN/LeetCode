class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort()
        while len(stones) > 1:
            last = stones[len(stones) - 1]
            second_to_last = stones[len(stones) - 2]
            if last == second_to_last:
                stones.pop()
                stones.pop()
            else:
                diff = last - second_to_last
                stones.pop()
                stones.pop()
                stones.append(diff)
                stones.sort()
        return stones[0] if len(stones) > 0 else 0

        