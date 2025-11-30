class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        max_ = max(arr1)
        count = [0] * (max_ + 1)

        for val in arr1:
            count[val] += 1
        
        res = [0] * len(arr1)
        ind = 0
        for val in arr2:
            while count[val] > 0:
                res[ind] = val
                ind += 1
                count[val] -= 1
        
        for index, value in enumerate(count):
            for i in range(value):
                res[ind] = index
                ind += 1
        
        return res




        # arr2ElementsRelativeOrder = {}
        # for i in range(len(arr2)):
        #     arr2ElementsRelativeOrder[arr2[i]] = i

        # arr1.sort()
        # for i in range(len(arr1)):
        #     if arr1[i] not in arr2ElementsRelativeOrder:
        #         arr2ElementsRelativeOrder[arr1[i]] = i + len(arr2)

        # def customeComparator(item):
        #     return arr2ElementsRelativeOrder[item]

        # arr1.sort(key = customeComparator)
        # return arr1


        