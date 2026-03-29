class Solution:
    def splitString(self, s: str) -> bool:  
        # ans = []
        # path = []

        # def backtrack(i):
        #     if i >= len(s):
        #         return

        #     path.append(s[i])
        #     backtrack(i+1)
        #     ans.append(path[:])

        #     path.pop()

        #     backtrack(i+1)
        
        # backtrack(0)
        # print(ans)
        # return True


        # def backtrack(path, i):
        #     if i >= len(s):
        #         for ind in range(1, len(path)):
        #             if int(path[ind]) != int(path[ind-1]) - 1:
        #                 return False
        #         return len(path) >= 2


        #     for j in range(i, len(s)):
        #         val = s[i:j+1]
        #         path.append(val)
        #         if backtrack(path, j+1):
        #             return True
                
        #         path.pop()

        #     return False
                
        # return backtrack([], 0)
        

        path = []
        def backtrack(i):
            if i >= len(s):
                for k in range(1, len(path)):
                    if int(path[k]) != int(path[k-1]) - 1:
                        return False

                return len(path) >= 2


            for j in range(i, len(s)):
                curr = s[i:j+1]

                if path and int(curr) != int(path[-1]) - 1:
                    continue

                path.append(curr)
                if backtrack(j+1):
                    return True
                path.pop()

            return False

        return backtrack(0)














