class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = Counter(nums1)
        ans = []
        for i in range(len(nums2)):
            if nums2[i] in count1 and count1[nums2[i]] > 0:
                ans.append(nums2[i])
                count1[nums2[i]] -= 1
        
        return ans




        
        # nums1.sort()
        # nums2.sort()
        # i, j = 0, 0
        # ans = []
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] > nums2[j]:
        #         j += 1
        #     elif nums1[i] < nums2[j]:
        #         i += 1
        #     else:
        #         ans.append(nums1[i])
        #         i += 1
        #         j += 1
        # return ans


        # nums1.sort()
        # nums2.sort()

        # l = r = 0
        # res = []
        # while l < len(nums1) and r < len(nums2):
        #     if nums1[l] == nums2[r]:
        #         res.append(nums1[l])
        #         l += 1
        #         r += 1
        #     elif nums1[l] < nums2[r]:
        #         l += 1
        #     else:
        #         r += 1
        # return res