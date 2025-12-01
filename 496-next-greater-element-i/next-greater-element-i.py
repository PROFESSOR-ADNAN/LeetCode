class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums1)):
            j = 0
            while nums2[j] != nums1[i]:
                j += 1
            
            for k in range(j+1, len(nums2)):
                if nums2[k] > nums1[i]:
                    ans.append(nums2[k])
                    break
            else:
                ans.append(-1)

        return ans