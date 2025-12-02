class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        maxQ = deque()
        minQ = deque()
        start = 0
        max_len = 0
        for end, num in enumerate(nums):
            while maxQ and maxQ[-1] < num:
                maxQ.pop()
            while minQ and minQ[-1] > num:
                minQ.pop()

            maxQ.append(num)
            minQ.append(num)

            while maxQ[0] - minQ[0] > limit:
                val = nums[start]
                if maxQ[0] == val:
                    maxQ.popleft()
                if minQ[0] == val:
                    minQ.popleft()
                start += 1
            max_len = max(max_len, end-start+1)
            
        return max_len
       
        # q = deque()
        # max_len = 0
        # for num in nums:
        #     while q and q[0] - num > limit:
        #         q.popleft()

        #     while q and q[-1] < num:
        #         max_len = max(max_len, len(q)+1)
        #         q.pop()
            
        #     q.append(num)

        # return max_len