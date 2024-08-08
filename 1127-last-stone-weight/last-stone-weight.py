class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            last = heapq.heappop(stones)
            second_to_last = heapq.heappop(stones)
            if last != second_to_last:
                diff = last - second_to_last
                heapq.heappush(stones, diff)
        stones.append(0)
        return abs(stones[0])
        