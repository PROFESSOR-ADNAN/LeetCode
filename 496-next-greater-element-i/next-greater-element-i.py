class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            curr = -1
            for j in range(len(nums2)):
                if num == nums2[j]:
                    for k in range(j+1, len(nums2)):
                        if  nums2[k] > num:
                            curr = nums2[k]
                            break
            ans.append(curr)

        return ans