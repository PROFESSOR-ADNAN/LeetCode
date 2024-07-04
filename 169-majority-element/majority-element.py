class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_map = {}

        for i in range(len(nums)):
            if nums[i] in count_map:
                count_map[nums[i]] += 1
            else:
                count_map[nums[i]] = 1
        
        max_count = 0
        for i in range(len(nums)):
            if count_map[nums[i]] > max_count:
                max_count = count_map[nums[i]]
                majority_num = nums[i]
        
        return majority_num