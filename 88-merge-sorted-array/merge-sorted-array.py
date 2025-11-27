class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        n1 = m - 1
        n2 = n - 1
        p = m + n - 1

        while n1 >= 0 and n2 >= 0:
            if nums1[n1] > nums2[n2]:
                nums1[p] = nums1[n1]
                n1 -= 1
            else:
                nums1[p] = nums2[n2]
                n2 -= 1
            p -= 1

        print("after the while loop", nums1)

        while n1 >= 0:
            nums1[p] = nums1[n1]
            n1 -= 1
            p -= 1
        while n2 >= 0:
            nums1[p]  = nums2[n2]
            n2 -= 1
            p -= 1


       
       
       
       
       
       
       
       
       
       
        # i = m-1
        # j = n-1
        # k = m+n-1
        # while i >= 0 and j >= 0:
        #     if nums1[i] > nums2[j]:
        #         nums1[k] = nums1[i]
        #         i -= 1
        #     else:
        #         nums1[k] = nums2[j]
        #         j -= 1
        #     k -= 1
        # while j >= 0:
        #     nums1[k] = nums2[j]
        #     j -= 1
        #     k -= 1

        # i = m-1
        # j = n-1
        # k = m+n-1
        # while i >= 0 and j >= 0:
        #     if nums1[i] > nums2[j]:
        #         nums1[k] = nums1[i]
        #         i -= 1
        #     else:
        #         nums1[k] = nums2[j]
        #         j -= 1
        #     k -= 1

        # while j >= 0:
        #     nums1[k] = nums2[j]
        #     j -= 1
        #     k -= 1

        
        # # for i in range(n):
        # #     nums1[m+i] = nums2[i]
        # # nums1.sort()