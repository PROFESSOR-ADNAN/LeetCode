class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge_sort(nums):
            if len(nums) > 1:
                mid = len(nums) // 2
                left_list = nums[:mid]
                right_list = nums[mid:]
                merge_sort(left_list)
                merge_sort(right_list)
                l = r = k = 0
                while l < len(left_list) and r < len(right_list):
                    if left_list[l] < right_list[r]:
                        nums[k] = left_list[l]
                        k += 1
                        l += 1
                    else:
                        nums[k] = right_list[r]
                        k += 1
                        r += 1
                while l < len(left_list):
                    nums[k] = left_list[l]
                    k += 1
                    l += 1
                while r < len(right_list):
                    nums[k] = right_list[r]
                    k += 1
                    r += 1
            return nums
        return merge_sort(nums)
            

        

        

        