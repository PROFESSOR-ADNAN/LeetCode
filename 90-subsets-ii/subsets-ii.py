class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sett = set()
        ans = []
        path = []

        def backtrack(i):
            if i >= len(nums):
                curr = path[:]
                curr.sort()
                if (tuple(curr)) not in sett:
                    ans.append(path[:])

                sett.add(tuple(curr))
                return

            
            path.append(nums[i])
            backtrack(i+1)
            path.pop()

            backtrack(i+1)

        backtrack(0)
        return ans