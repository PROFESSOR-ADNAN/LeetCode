class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        arr2ElementsRelativeOrder = {}
        for i in range(len(arr2)):
            arr2ElementsRelativeOrder[arr2[i]] = i

        arr1.sort()
        for i in range(len(arr1)):
            if arr1[i] not in arr2ElementsRelativeOrder:
                arr2ElementsRelativeOrder[arr1[i]] = i + len(arr2)

        def customeComparator(item):
            return arr2ElementsRelativeOrder[item]

        arr1.sort(key = customeComparator)
        return arr1


        