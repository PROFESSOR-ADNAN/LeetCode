class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        n = len(nums)
        nums.sort()

        if not nums:
            return 0

        l = 0
        r = 1
        duplicate = 0

        while r < n:
            if nums[r] == nums[r-1] + 1:
                r += 1
            elif nums[r] == nums[r-1]:
                duplicate += 1
                r += 1
            else:
                print(r, duplicate)
                max_len = max(max_len, r-l-duplicate)
                l = r
                r += 1
                duplicate = 0

        max_len = max(max_len, r-l-duplicate)
        return max_len

