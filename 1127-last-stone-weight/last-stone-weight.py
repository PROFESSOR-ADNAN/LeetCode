class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            heapq._heapify_max(stones)
            max = heapq.heappop(stones)
            heapq._heapify_max(stones)
            second_max = heapq.heappop(stones)

            if max != second_max:
                heapq.heappush(stones, max - second_max)
        return stones[0] if len(stones) > 0 else 0

        