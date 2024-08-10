class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        min_heap = []
        for num, freq in count.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, num))
            else:
                heapq.heappushpop(min_heap, (freq, num))
        ans = []
        for _, num in min_heap:
            ans.append(num)
        return ans



        
     
        