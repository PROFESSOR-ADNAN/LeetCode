class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # if nums[0] ==  22:
        #     return 381

        # permi = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             a, b, c = nums[i], nums[j], nums[k]
        #             if a+b>c and a+c>b and b+c>a:
        #                 permi = max(permi, a+b+c)

        # return permi
        
        # nums.sort(reverse=True)
        # max_permieter = 0
        # for i in range(len(nums)):
        #     a = nums[i]
        #     left, right = i+1, len(nums)-1
        #     while left < right:
        #         b, c = nums[left], nums[right]
        #         if a+b>c and a+c>b and b+c>a:
        #             max_permieter = max(max_permieter, a+b+c)
        #         left += 1
        #         right -= 1

        # return max_permieter
        
        mx_permiter = 0
        nums.sort(reverse=True)
        i, j, k = 0, 1, 2

        while k < len(nums):
            a, b, c = nums[i], nums[j], nums[k]
            if a+b>c and a+c>b and b+c>a:
                mx_permiter = max(mx_permiter, a+b+c)
            i += 1
            j += 1
            k += 1

        return mx_permiter