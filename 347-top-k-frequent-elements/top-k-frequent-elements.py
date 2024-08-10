class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        max_heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(max_heap)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(max_heap)[1])
        return ans



        
     
        