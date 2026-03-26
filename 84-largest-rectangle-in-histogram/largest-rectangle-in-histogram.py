class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack = []
        # maxArea = 0
        # for i in range(len(heights)):
        #     height = heights[i]
        #     start = i
        #     while stack and stack[-1][0] > height:
        #         curr, index = stack.pop()
        #         maxArea = max(maxArea, (i - index) * height)
        #         if height <= curr:
        #             start = index
        #     stack.append([height, start])

        # return maxArea


        # stack = []
        # maxArea = 0

        # for ind, height in enumerate(heights):
        #     start = ind
        #     while stack and stack[-1][0] > height:
        #         currHeight, currIndex = stack.pop()
        #         maxArea = max(maxArea, (ind - currIndex) * currHeight)
        #         start = currIndex

        #     stack.append([height, start])

        # while stack:
        #     currHeight, currIndex = stack.pop()
        #     maxArea = max(maxArea, (len(heights) - currIndex) * currHeight)

        # return maxArea

        # nse = {}
        # def nextSE():
        #     stack = []
        #     for i in range(len(heights)):
        #         height = heights[i]
        #         while stack and heights[stack[-1]] > height:
        #             nse[stack.pop()] = i

        #         stack.append(i)

        #     while stack:
        #         nse[stack.pop()] = len(heights)

        # pse = {}
        # def prevSE():
        #     stack = []
        #     for i in range(len(heights)):
        #         height = heights[i]
        #         while stack and heights[stack[-1]] > height:
        #             stack.pop()

        #         if not stack:
        #             pse[i] = -1
        #         else:
        #             pse[i] = stack[-1]

        #         stack.append(i)
        
        # prevSE()
        # nextSE()

        # maxArea = 0
        # for i in range(len(heights)): 
        #     maxArea = max(maxArea, (nse[i]-pse[i]-1)*heights[i])

        # return maxArea

        stack = []
        maxArea = 0

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][0] > height:
                currHeight, currIndex = stack.pop()
                maxArea = max(maxArea, (i - currIndex) * currHeight)
                start = currIndex

            stack.append([height, start])

        while stack:
            currHeight, currIndex = stack.pop()
            maxArea = max(maxArea, (len(heights) - currIndex) * currHeight)

        return maxArea
