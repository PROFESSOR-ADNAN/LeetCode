class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sett = set()
        # ans = []
        # path = []

        # def backtrack(i):
        #     if i >= len(nums):
        #         curr = path[:]
        #         curr.sort()
        #         if (tuple(curr)) not in sett:
        #             ans.append(path[:])

        #         sett.add(tuple(curr))
        #         return

            
        #     path.append(nums[i])
        #     backtrack(i+1)
        #     path.pop()

        #     backtrack(i+1)

        # backtrack(0)
        # return ans


        ans = []
        path = []

        nums.sort()

        def backtrack(i):
            if i >= len(nums):
                ans.append(path[:])
                return

            path.append(nums[i])
            backtrack(i+1)
            path.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            backtrack(i+1)

        backtrack(0)
        return ans