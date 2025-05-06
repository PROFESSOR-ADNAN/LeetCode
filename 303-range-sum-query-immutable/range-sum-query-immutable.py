class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        


    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # return sum(self.nums[left:right+1])
        if left:
            return self.nums[right] - self.nums[left-1]
        return self.nums[right]
        
   
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)