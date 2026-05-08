class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones.sort()
        # while len(stones) > 1:
        #     a = stones.pop()
        #     b = stones.pop()
        #     if a != b:
        #         stones.append(a-b)
        #     stones.sort()

        # return stones[0]

        maxHeap = [-val for val in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            a = -1 * heapq.heappop(maxHeap)
            b = -1 * heapq.heappop(maxHeap)

            if a != b:
                # maxHeap.append(-1 * (a-b))
                # heapq.heapify(maxHeap)
                heapq.heappush(maxHeap, -(a-b))

        return -maxHeap[0] if maxHeap else 0