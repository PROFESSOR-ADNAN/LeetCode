class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        count = Counter(nums)
        for i in range(len(nums)):
            if nums[i] + 1 in count:
                lenght = count[nums[i]] + count[nums[i] + 1]
                max_len = max(max_len, lenght)
        
        return max_len
