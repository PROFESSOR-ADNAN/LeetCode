class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        def backtrack(i):
            if len(path) >= 2 and path not in ans:
                for j in range(1, len(path)):
                    if path[j] < path[j-1]:
                        return
                ans.append(path[:])
            
            if i >= len(nums):
                return



            path.append(nums[i])
            backtrack(i+1)
            path.pop()

            backtrack(i+1)

        backtrack(0)
        return ans

