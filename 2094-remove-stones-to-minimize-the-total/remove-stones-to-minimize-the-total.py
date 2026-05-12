class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxHeap = [-num for num in piles]

        heapq.heapify(maxHeap)

        for _ in range(k):
            curr = -1 * heapq.heappop(maxHeap)

            calc = curr - (curr // 2)
            heapq.heappush(maxHeap, -1 * calc)

        return sum([-1 * val for val in maxHeap])