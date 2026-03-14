class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # stack = []

        # for log in logs:
        #     if log == "../":
        #         if stack: stack.pop()
        #     elif log == "./":
        #         continue
        #     else:
        #         stack.append(log)

        # return len(stack)

        ans = 0
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                # if ans > 0: ans -= 1
                ans = max(0, ans - 1)
            else:
                ans += 1

        return ans
                
