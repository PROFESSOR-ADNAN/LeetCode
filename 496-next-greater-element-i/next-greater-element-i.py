class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # ans = []
        # for num in nums1:
        #     curr = -1
        #     for j in range(len(nums2)):
        #         if num == nums2[j]:
        #             for k in range(j+1, len(nums2)):
        #                 if  nums2[k] > num:
        #                     curr = nums2[k]
        #                     break
        #     ans.append(curr)

        # return ans

        # stack = []
        # ans = defaultdict(lambda:-1)

        # for num in nums2:
        #     while stack and stack[-1] < num:
        #         ans[stack[-1]] = num
        #         stack.pop()

        #     stack.append(num)

        # answer = []
        # for num in nums1:
        #     answer.append(ans[num])

        # return answer


        stack = []
        mpp = defaultdict(lambda : -1)
        for num in nums2:
            while stack and stack[-1] < num:
                mpp[stack[-1]] = num
                stack.pop()

            stack.append(num)

        for i in range(len(nums1)):
            nums1[i] = mpp[nums1[i]]

        return nums1
