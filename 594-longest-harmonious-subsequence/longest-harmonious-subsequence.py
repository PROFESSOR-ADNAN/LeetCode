class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        max_len = 0
        for num in nums:
            if num+1 in count:
                max_len = max(max_len, count[num] + count[num+1])
        
        return max_len
