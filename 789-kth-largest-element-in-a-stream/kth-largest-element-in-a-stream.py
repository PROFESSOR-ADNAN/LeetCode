class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []
        for num in nums:
            if len(self.minHeap) < self.k:
                heappush(self.minHeap, num)
            else:
                curr_top = heappop(self.minHeap)
                heappush(self.minHeap, max(curr_top, num))

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heappush(self.minHeap, val)
        else:
            curr_top = heappop(self.minHeap)
            heappush(self.minHeap, max(curr_top, val))

        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)