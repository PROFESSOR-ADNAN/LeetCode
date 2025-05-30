class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """ 
        max_value = max(nums)
        count = [0] * (max_value + 1)
        for i in range(len(nums)):
            count[nums[i]] += 1
        for i in range(1, len(count)):
            count[i] += count[i-1]
        
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = 0
            else:
                nums[i] = count[nums[i]-1] 
        return nums


        # ind = []
        # for i in range(len(nums)):
        #     ind.append([nums[i], i])
        # ind.sort()
        
        # nums[ind[0][1]] = 0
        # for i in range(1, len(nums)):
        #     if ind[i][0] != ind[i-1][0]:
        #         nums[ind[i][1]] = i
        #     else:
        #         nums[ind[i][1]] = nums[ind[i-1][1]]
        
        # return nums


        # ans = []
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         if nums[i] > nums[j]:
        #             count += 1
        #     ans.append(count)
        # return ans




        # max_value = max(nums) 
        # min_value = min(nums)
        # range_value = max_value - min_value + 1

        # count = [0] * range_value
        # for num in nums:
        #     count[num-min_value] += 1

        # for i in range(1, len(count)):
        #     count[i] += count[i-1]

        # for i in range(len(nums)):
        #     if nums[i] == min_value:
        #         nums[i] = 0
        #     else:
        #         nums[i] = count[nums[i] - min_value - 1]
        # return nums