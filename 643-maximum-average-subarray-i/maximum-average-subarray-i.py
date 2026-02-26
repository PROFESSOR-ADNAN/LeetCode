class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = 0, k
        curr = sum(nums[:r])
        mx_sum = curr

        print(l, r, mx_sum, curr)
        while r < len(nums):
            curr += nums[r]
            curr -= nums[l]
            mx_sum = max(mx_sum, curr)

            r += 1
            l += 1

        return mx_sum/k
