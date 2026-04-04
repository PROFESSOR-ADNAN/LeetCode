class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # ans = []
        # i = j = 0

        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] < nums2[j]:
        #         ans.append(nums1[i])
        #         i += 1
        #     else:
        #         ans.append(nums2[j])
        #         j += 1
        
        # ans.extend(nums1[i:])
        # ans.extend(nums2[j:])

        # n = len(ans)
        # half = n // 2

        # if n % 2:
        #     return float(ans[half])
        # else:
        #     a, b = ans[half], ans[half-1]
        #     return (a+b) / 2

        def helper(nums1, nums2):
            n, m = len(nums1), len(nums2)
            if n > m: return helper(nums2, nums1)

            total = (n+m)
            total_left = (n+m+1) // 2
            left, right = 0, n

            a = nums1
            b = nums2

            while left <= right:
                mid1 = left + (right - left) // 2
                mid2 = total_left - mid1

                l1 = a[mid1-1] if mid1-1 >= 0 else float("-inf")
                l2 = b[mid2-1] if mid2-1 >= 0 else float("-inf")
                r1 = a[mid1] if mid1 < n else float("inf")
                r2 = b[mid2] if mid2 < m else float("inf")

                if l1 <= r2 and l2 <= r1:
                    if (total % 2): return max(l1, l2)
                    else: return (max(l1, l2) + min(r1, r2)) / 2
                elif l1 > r2: right = mid1 - 1
                else: left = mid1 + 1

        return helper(nums1, nums2)
