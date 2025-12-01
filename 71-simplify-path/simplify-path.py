class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        i = 0
        while i < len(path):
            while i < len(path) and path[i] == "/":
                i += 1
                continue
            cur = ""
            while i < len(path) and path[i] != "/":
                cur += path[i]
                i += 1
            if cur == "..":
                if stack:
                    stack.pop()
                else:
                    continue
            elif cur == ".":
                continue
            elif cur:
                stack.append(cur)

        ans = "/"
        for path in stack:
            ans += path + "/"

        return ans[:-1] if len(ans) > 1 else ans










        # arr = list(path.split(" / "))
        # print(arr)
        