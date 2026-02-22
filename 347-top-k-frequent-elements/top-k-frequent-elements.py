class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = Counter(nums)
        # freq = []

        # for num, frequency in count.items():
        #     freq.append([frequency, num])

        # freq.sort()
        # ans = []
        # ind = 0

        # while k > 0:
        #     ans.append(freq[ind][1])

        # return ans

        count = Counter(nums)
        maxHeap = []
        for key, value in count.items():
            maxHeap.append([value * -1, key])

        heapq.heapify(maxHeap)
        
        ans = []
        while k > 0:
            ans.append(heapq.heappop(maxHeap)[1])
            k -= 1
        
        return ans

