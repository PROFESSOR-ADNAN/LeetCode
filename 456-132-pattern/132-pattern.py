class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             if nums[i] < nums[k] < nums[j]:
        #                 return True

        # return False
        
        # n = len(nums)
        # if n < 3: return False

        # mx = 0
        # mxInd = -1

        # for i in range(len(nums)):
        #     if nums[i] > mx:
        #         mx = nums[i]
        #         mxInd = i

        # if mxInd != 0 and mxInd != n-1: return True
        # else: return False

        # n = len(nums)
        # mx = max(nums)
        # mxInd = nums.index(mx)
        # mnb4mx = float("inf")
        # if mxInd > 0:
        #     mnb4mx = min(nums[:mxInd])
        # mxa4mx = float("-inf")
        # if mxInd < n-1:
        #     mxa4mx = max(nums[mxInd+1:])

        # return mxa4mx > mnb4mx and mxa4mx != mx and mnb4mx != mx


        # stack = []
        # mn = float("inf")
        
        # for num in nums:
        #     while stack and stack[-1] <= num:
        #         mn = min(mn, stack[-1])
        #         stack.pop()

        #     if stack and num > mn:
        #         return True

        #     stack.append(num)

        # return False


        stack = []
        currMin = nums[0]

        for num in nums[1:]:
            while stack and stack[-1][0] <= num:
                stack.pop()

            if stack and num > stack[-1][1]:
                return True

            stack.append([num, currMin])
            currMin = min(currMin, num)

        return False