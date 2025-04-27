class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ind = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[ind] = nums[i]
                ind += 1
        return ind

        # newNums= []
        # for i in range(len(nums)):
        #     if nums[i] not in newNums:
        #         newNums.append(nums[i])
        
        # for i in range(len(newNums)):
        #     nums[i] = newNums[i]
        
        # return len(newNums)


        # index = 1
        # n = len(nums)
        # for i in range(1, n):
        #     if nums[i] != nums[i-1]:
        #         nums[index] = nums[i]
        #         index += 1
        # return index