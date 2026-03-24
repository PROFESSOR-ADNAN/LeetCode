class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(path, visited):
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for ind in range(len(nums)):
                if visited[ind]:
                    continue

                path.append(nums[ind])
                visited[ind] = True
                backtrack(path, visited)
                path.pop()
                visited[ind] = False
    
        backtrack([], [False]*len(nums))
        return ans