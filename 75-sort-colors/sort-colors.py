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

        # count = [0] * 3
        # for num in nums:
        #     count[num] += 1

        # ind = 0
        # for num, cnt in enumerate(count):
        #     for _ in range(cnt):
        #         nums[ind] = num
        #         ind += 1

        # left, right = 0, len(nums)-1
        # for i, num in enumerate(nums):
        #     print(nums)
        #     if num == 0:
        #         nums[left], nums[i] = nums[i], nums[left]
        #         left += 1
        #     elif num == 2 and nums[right] == 0:
        #         nums[right], nums[left] = nums[left], nums[right]
        #         left += 1
        #         right -= 1
        #     elif num == 2:
        #         nums[right], nums[i] = nums[i], nums[right]
        #         right -= 1


        #     print(nums)
        #     print()

        left, right = 0, len(nums)-1
        ind = 0

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        while ind <= right:
            if nums[ind] == 0:
                swap(ind, left)
                left += 1

            elif nums[ind] == 2:
                swap(ind, right)
                right -= 1
                ind -= 1
                
            ind += 1
