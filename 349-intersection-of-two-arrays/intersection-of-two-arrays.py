class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = set()
        for num in nums1:
            if num in nums2:
                intersection.add(num)
        return intersection