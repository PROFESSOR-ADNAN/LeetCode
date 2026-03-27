class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # ans = []
        # def backtrack(path):
        #     if len(path) == len(nums):
        #         ans.append(path[:])
        #         return

        #     for i in range(len(nums)):
        #         if nums[i] in path:
        #             continue

        #         path.append(nums[i])
        #         backtrack(path)
        #         path.pop()
        
        # backtrack([])
        # return ans

        # ans = []
        # path = []

        # def backtrack():
        #     if len(path) == len(nums):
        #         ans.append(path[:])
        #         return

        #     for i in range(len(nums)):
        #         if nums[i] in path:
        #             continue

        #         path.append(nums[i])
        #         backtrack()
        #         path.pop()

        # backtrack()
        # return ans

        ans = []
        path = []

        def backtrack():
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                
                path.append(nums[i])
                backtrack()
                path.pop()

        backtrack()
        return ans
        
        