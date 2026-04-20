class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count = Counter(nums)
        # total = 0
        # for i in range(1, 3):
        #     if i not in nums:
        #         continue
        #     total += count[i-1]
        #     count[i] = total
        # count[0] = 0

        # print(count)
        # ans = [-1] * len(nums)
        # for ind, num in enumerate(nums):
        #     j = count[num]
        #     while j < len(ans) and ans[j] == num:
        #         j += 1

        #     # ans[j] = num

        # for i in range(len(nums)):
        #     nums[i] = ans[i]

        count = [0] * 3
        for num in nums:
            count[num] += 1

        ind = 0
        for num, cnt in enumerate(count):
            for _ in range(cnt):
                nums[ind] = num
                ind += 1

            
