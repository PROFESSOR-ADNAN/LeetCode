class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        arr = []
        for num  in nums:
            arr.append(num)
        for i in range(0, len(arr) - 1, 2):
            arr[i], arr[i+1] = arr[i+1], arr[i]        
        return arr