class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ans = []
        # for i in range(len(temperatures)):
        #     curr = 0
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             curr = j-i
        #             break
        #     ans.append(curr)

        # return ans

        n = len(temperatures)
        stack = []
        ans = [0] * n

        for i in range(n):
            temp = temperatures[i]
            while stack and stack[-1][0] < temp:
                ind = stack[-1][1]
                days = i - stack[-1][1]
                ans[ind] = days
                stack.pop()
            
            stack.append([temp, i])

        return ans



