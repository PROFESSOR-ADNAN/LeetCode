class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [x * -1 for x in stones]
        print(stones)
        heapq.heapify(stones)
        while len(stones) > 1:
            last = heapq.heappop(stones)
            second_to_last = heapq.heappop(stones)
            if last != second_to_last:
                diff = last - second_to_last
                heapq.heappush(stones, diff)
        return stones[0] * -1 if len(stones) > 0 else 0
        