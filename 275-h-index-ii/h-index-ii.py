class Solution:
    def hIndex(self, citations: List[int]) -> int:

        # def isValid(index):
        #     curr_citation = citations[index]
        #     return curr_citation >= index+1

        # low, high = 0, len(citations)-1
        # while low <= high:
        #     mid = low + (high - low) // 2
        #     if isValid(mid):
        #         high = mid - 1
        #     else:
        #         low = mid + 1

        # return citations[low]


        # def isValid(h):
        #     print(h, citations[h-1])
        #     return citations[h-1] >= h


        # low, high = 1, len(citations)
        # while low <= high:
        #     mid = low + (high - low) // 2
        #     if isValid(mid):
        #         low = mid
        #     else:
        #         high = mid - 1

        # return high

        citations.reverse()

        def isValid(h):
            return citations[h-1] >= h


        low, high = 1, len(citations)
        while low <= high:
            mid = low + (high - low) // 2
            if isValid(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high