class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        q = deque(nums)

        for i in range(len(nums)-k):
            q.append(q.popleft())
        for i in range(len(nums)):
            nums[i] = q.popleft()
            



        # rotate = nums[len(nums)-(k%len(nums)):]
        # rotate.extend(nums[:len(nums)-(k%len(nums))])
        # for i in range(len(rotate)):
        #     nums[i] = rotate[i]
            

