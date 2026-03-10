class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # n = len(nums)
        # max_len = 0
        # for i in range(n):
        #     min_, max_ = float("inf"), 0
        #     for j in range(i, n):
        #         max_ = max(max_, nums[j])
        #         min_ = min(min_, nums[j])

        #         if max_ - min_ <= limit:
        #             max_len = max(max_len, j-i+1)

        # return max_len

        # n = len(nums)
        # max_len = 0
        # minStack = deque()
        # maxStack = deque()

        # left = 0
        # for right in range(n):
            
        #     num = nums[right]

        #     while maxStack and maxStack[0] < num:
        #         maxStack.popleft()
        #     while maxStack and maxStack[-1] < num:
        #         maxStack.pop()
        #     maxStack.append(num)

        #     while minStack and minStack[0] > num:
        #         minStack.popleft()
        #     while minStack and minStack[-1] > num:
        #         minStack.pop()
        #     minStack.append(num)

        #     while maxStack and minStack and maxStack[0] - minStack[0] > limit:
        #         # minStack.pop(nums[left])
        #         # maxStack.pop(nums[left])
        #         element = nums[left]
        #         if maxStack[0] == element:
        #             maxStack.popleft()
        #         if minStack[0] == element:
        #             minStack.popleft()
        #         left += 1

        #     max_len = max(max_len, right - left + 1)

        # return max_len
            


        n = len(nums)
        max_len = 0
        minStack = deque()
        maxStack = deque()

        left = 0
        for right in range(n):
            
            num = nums[right]

            while maxStack and maxStack[-1] < num:
                maxStack.pop()
            maxStack.append(num)
            
            while minStack and minStack[-1] > num:
                minStack.pop()
            minStack.append(num)

            while maxStack and minStack and maxStack[0] - minStack[0] > limit:
                element = nums[left]
                if maxStack[0] == element:
                    maxStack.popleft()
                if minStack[0] == element:
                    minStack.popleft()
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
            




