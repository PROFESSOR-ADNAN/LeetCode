class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:  
            heapq._heapify_max(stones)
            last = heapq.heappop(stones)
            heapq._heapify_max(stones)
            second_to_last = heapq.heappop(stones)
            if last != second_to_last:
                diff = last - second_to_last
                stones.append(diff)
        return stones[0] if len(stones) > 0 else 0

        