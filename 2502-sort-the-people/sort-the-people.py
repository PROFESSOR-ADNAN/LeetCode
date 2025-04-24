class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        # bubble sort
        # for i in range(len(names)):
        #     for j in range(len(names)-1-i):
        #         if heights[j] < heights[j+1]:
        #             heights[j], heights[j+1] = heights[j+1], heights[j]
        #             names[j], names[j+1] = names[j+1], names[j]

        # return names

        # selection sort
        for i in range(len(names)):
            maxInd = i
            for j in range(i+1, len(names)):
                if heights[j] > heights[maxInd]:
                    maxInd = j
            heights[i], heights[maxInd] = heights[maxInd], heights[i]
            names[i], names[maxInd] = names[maxInd], names[i]

        return names


        # insertion sort


        # count sort

        # merge sort

        # quick sort