class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        warmerTemp = defaultdict(lambda: 0)
        for ind, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                warmerTemp[stack[-1][1]] = ind - stack[-1][1]
                stack.pop()
            stack.append([temp, ind])

        return [warmerTemp[i] for i in range(len(temperatures))]