class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # k = len(nums) - k
        # def quickSelect(l, r):
        #     pivot, p = nums[r], l
        #     for i in range(l, r):
        #         if nums[i] <= pivot:
        #             nums[i], nums[p] = nums[p], nums[i]
        #             p += 1
        #     nums[p], nums[r] = pivot, nums[p]
        #     if p > k: return quickSelect(l, p-1)
        #     elif p < k: return quickSelect(p+1, r)
        #     else: return nums[p]
    
        # return quickSelect(0, len(nums)-1)
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for i in range(k):
            itm = heapq.heappop(nums)
        return itm * -1        