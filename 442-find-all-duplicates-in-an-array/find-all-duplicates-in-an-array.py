# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         ans = []
#         for i in range(len(nums)):
#             num = nums[i]
#             if (num in nums[:i] or num in nums[i+1:]) and num not in ans:
#                 ans.append(num)

#         return ans

# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         ans = []
#         n = len(nums)

#         for i in range(1, n+1):
#             if nums.count(i) > 1:
#                 ans.append(i)
        
#         return ans


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        firstTime = set()
        secondTime = set()
        n = len(nums)

        for num in nums:
            if num not in firstTime:
                firstTime.add(num)
            else:
                secondTime.add(num)

        return list(secondTime)


