class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        Map = {}
        count = 0
        for i, num in enumerate(nums):
            if num in Map:
                for ind in Map[num]:
                    if (ind * i) % k == 0:
                        count += 1
                Map[num].append(i)
            else:
                Map[num] = [i]
        return count




        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j] and (i*j) % k == 0:
        #             count += 1
        # return count
        