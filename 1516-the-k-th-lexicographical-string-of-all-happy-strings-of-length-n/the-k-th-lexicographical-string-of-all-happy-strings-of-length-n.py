class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        char = ["a", "b", "c"]
        ans = []
        path = []

        def backtrack():
            if len(path) == n:
                ans.append(path[:])
                return

            for j in range(3):
                if path and path[-1] == char[j]:
                    continue

                path.append(char[j])
                backtrack()
                path.pop()

        backtrack()

        if k <= len(ans):
            return "".join(ans[k-1])
        else:
            return ""




            
