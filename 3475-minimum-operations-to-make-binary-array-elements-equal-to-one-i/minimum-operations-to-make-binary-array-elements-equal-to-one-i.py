class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # n = len(nums)
        # operation = 0
        # for i in range(n-2):
        #     if nums[i] == 0:
        #         nums[i] = 1
        #         operation += 1
        #         for j in range(i+1, i+3):
        #             if nums[j] == 0:
        #                 nums[j] = 1
        #             else:
        #                 nums[j] = 0

        # if sum(nums) == len(nums):
        #     return operation
        # else:
        #     return -1

        # def flip(nums, i):
        #     nums[i] = 0 if nums[i] else 1

        # n = len(nums)
        # operation = 0
        # for i in range(n-2):
        #     if nums[i] == 0:
        #         flip(nums, i)
        #         flip(nums, i+1)
        #         flip(nums, i+2)

        #         operation += 1  
        
        # print(nums)
        # if not nums[-1] or not nums[-2]:
        #     return -1

        # return operation


        def flip(nums, i):
            nums[i] ^= 1
            nums[i+1] ^= 1
            nums[i+2] ^= 1

        n = len(nums)
        operation = 0
        for i in range(n-2):
            if nums[i] == 0:
                flip(nums, i)
                operation += 1  
        
        if not nums[-1] or not nums[-2]:
            return -1

        return operation