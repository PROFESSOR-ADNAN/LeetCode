class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        right_sum = sum(nums)
        left_sum = 0
        max_sum = right_sum
        Map = {max_sum:[0]}
        for i in range(len(nums)):
            if nums[i] == 0:
                left_sum += 1
            right_sum -= nums[i]
            max_sum = max(max_sum, left_sum + right_sum)
            if max_sum == (left_sum + right_sum) and max_sum in Map:
                Map[max_sum].append(i+1)
            elif max_sum == (left_sum + right_sum):
                Map[max_sum] = [i+1]
        return Map[max(Map)]
            