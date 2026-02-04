class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # // considers the entires interval to be valid for left and right

        # ranges.sort()
        # print(ranges)
        # if (left >= ranges[0][0] and 
        #     right <= ranges[-1][1]):
        #     return True
        # return False

        # for start, end in ranges:
        #     if left >= start and right <= end:
        #         return True
        
        # return False

        ranges.sort()
        ind = 0
        for val in range(left, right+1):
            found = False
            while ind < len(ranges):
                if val < ranges[ind][0]:
                    return False
                elif ranges[ind][0] <= val <= ranges[ind][1]:
                    found = True
                    break
                else:
                    found = False
                    ind += 1

        return True if found else False

        
