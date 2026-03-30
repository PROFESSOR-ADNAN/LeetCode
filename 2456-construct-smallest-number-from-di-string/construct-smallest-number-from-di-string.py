class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        # ans = []
        # path = []

        # def backtrack(i, j):
        #     if len(path) == len(pattern):
        #         ans.append(path[:])
        #         return
        #     if j < 0 or j > len(pattern):
        #         return
        #     if i >= len(pattern):
        #         return

        #     curr = pattern[i]
        #     if curr == "I":
        #         while choices[j] in path:
        #             j += 1
        #         if j >= len(pattern):
        #             return
        #         path.append(choices[j])
        #         backtrack(i+1, j+1)
        #         path.pop()
        #     else:
        #         while choices[j] in path:
        #             j -= 1
        #         if j < 0:
        #             return
        #         path.append(choices[j])
        #         backtrack(i+1, j-1)
        #         path.pop()

        # backtrack(0, 0)
        # print(ans)
        # return ""


        # nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        # path = []
        # ans = []

        # def backtrack(i):
        #     if len(path) == len(pattern) + 1:
        #         for k in range(len(path)-1):
        #             curr = pattern[k]
        #             if curr == "I":
        #                 if int(path[k]) >= int(path[k+1]):
        #                     return False
        #             else:
        #                 if int(path[k]) <= int(path[k+1]):
        #                     return False

        #         ans.append(path[:])

        #     for j in range(i, len(pattern)+1):
        #         path.append(nums[j])
        #         if backtrack(j+1):
        #             return "".join(path)
        #         path.pop()

        # backtrack(0)
        # print(ans)
        # return ""

        nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        path = []

        def backtrack(i):
            if i == len(pattern) + 1:
                for k in range(len(path)-1):
                    curr = pattern[k]
                    if curr == "I":
                        if int(path[k]) >= int(path[k+1]):
                            return False
                    else:
                        if int(path[k]) <= int(path[k+1]):
                            return False
                return True

            for j in range(len(nums)):
                if nums[j] in path:
                    continue

                path.append(nums[j])
                if backtrack(i+1):
                    return "".join(path)
                path.pop()

        return backtrack(0)