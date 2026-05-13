class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        heapq.heapify(minHeap)

        for num in nums:
            if len(minHeap) < k:
                heappush(minHeap, num)
            else:
                smallest_in_heap = heapq.heappop(minHeap)
                if smallest_in_heap < num:
                    heapq.heappush(minHeap, num)
                else:
                    heapq.heappush(minHeap, smallest_in_heap)

        return heapq.heappop(minHeap)
