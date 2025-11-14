class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        for num in range(left, right+1):
            covered = False
            for x, y in ranges:
                if x <= num <= y:
                    covered = True
                    break
            if not covered:
                return False

        return True












        # for i in range(len(ranges)):
        #     x, y = ranges[i][0], ranges[i][1]
        #     print(x, y)
        #     if left == x:
        #         left += 1
        #     if left == y:
        #         left += 1
        #     print("first", left)
        #     if left >= right + 1:
        #         print("yes")
        #         return True
        #     print(left)

        # return False
        