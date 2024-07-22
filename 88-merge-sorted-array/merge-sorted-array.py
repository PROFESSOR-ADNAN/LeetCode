class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        left = right = k = 0
        left_list = nums1[:m+1]
        while left < m and right < n:
            if left_list[left] < nums2[right]:
                nums1[k] = left_list[left]
                left += 1
                k += 1
            else:
                nums1[k] = nums2[right]
                right += 1
                k += 1
        while left < m:
            nums1[k] = left_list[left]
            left += 1
            k += 1
        while right < n:
            nums1[k] = nums2[right]
            right += 1
            k += 1
        return nums1