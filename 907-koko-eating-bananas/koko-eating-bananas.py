class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def Possible(val):
            time = 0
            for pile in piles:
                time += math.ceil(pile / val)
            return time <= h

        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            if Possible(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low