class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for itm in freq[i]:
                ans.append(itm)
                if len(ans) == k:
                    return ans



        
     
        