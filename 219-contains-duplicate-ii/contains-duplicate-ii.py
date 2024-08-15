class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        indexed_arr = [(nums[i], i) for i in range(len(nums))]
        indexed_arr.sort()
        for i in range(len(indexed_arr)-1):
            if indexed_arr[i][0] == indexed_arr[i+1][0] and abs(indexed_arr[i][1] - indexed_arr[i+1][1]) <= k:
                return True

        return False
        