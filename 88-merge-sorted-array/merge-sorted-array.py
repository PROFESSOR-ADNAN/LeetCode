class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums3 = []
        left = 0
        right = 0
        while left < m and right < n:
            if nums1[left] <= nums2[right]:
                nums3.append(nums1[left])
                left += 1
            else:
                nums3.append(nums2[right])
                right += 1
        while left < m:
            nums3.append(nums1[left])
            left += 1
        while right < n:
            nums3.append(nums2[right])
            right += 1
        for i in range(n+m):
            nums1[i] = nums3[i]
        return nums1