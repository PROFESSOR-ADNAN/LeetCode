class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # compeleteNums = [i for i in range(len(nums)+1)]

        # for num in compeleteNums:
        #     if num not in nums:
        #         return num

        n = len(nums)

        max_of_nums = max(nums)
        sum_of_nums = sum(nums)
        sum_of_all_nums = (n * (n+1))//2
        
        return sum_of_all_nums - sum_of_nums
