class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        for i in range(1, len(nums), 2):
            nums[i], nums[i-1] = nums[i-1], nums[i]

        return nums











        # nums.sort()
        # arr = []
        # for num  in nums:
        #     arr.append(num)
        # for i in range(0, len(arr), 2):
        #     arr[i], arr[i+1] = arr[i+1], arr[i]        
        # return arr