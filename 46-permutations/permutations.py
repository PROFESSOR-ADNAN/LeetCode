class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(path, ind):
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for ind in range(len(nums)):
                if nums[ind] in path:
                    continue

                path.append(nums[ind])
                backtrack(path, ind+1)
                path.pop()
    
        backtrack([], 0)
        return ans