class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        nextGreaterElement = {}
        for num in nums2[::-1]:
            while stack and stack[-1] <= num:
                stack.pop()
            nextGreaterElement[num] = -1 if not stack else stack[-1]
            stack.append(num)  

        return [nextGreaterElement[num] for num in nums1] 

        
        
        # ans = []
        # for i in range(len(nums1)):
        #     j = 0
        #     while nums2[j] != nums1[i]:
        #         j += 1
            
        #     for k in range(j+1, len(nums2)):
        #         if nums2[k] > nums1[i]:
        #             ans.append(nums2[k])
        #             break
        #     else:
        #         ans.append(-1)

        # return ans