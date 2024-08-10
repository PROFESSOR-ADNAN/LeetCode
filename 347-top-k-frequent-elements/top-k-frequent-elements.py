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
        return [itm[0] for itm in freq[:k]]



        
     
        