class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        freq = [(num, cnt) for num, cnt in count.items()]
        freq.sort(key=lambda x: -x[1])
        ans = []
        for i in range(k):
            ans.append(freq[i][0])
        return ans



        
     
        