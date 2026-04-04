class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = []
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        
        ans.extend(nums1[i:])
        ans.extend(nums2[j:])

        n = len(ans)
        half = n // 2

        if n % 2:
            return float(ans[half])
        else:
            a, b = ans[half], ans[half-1]
            return (a+b) / 2