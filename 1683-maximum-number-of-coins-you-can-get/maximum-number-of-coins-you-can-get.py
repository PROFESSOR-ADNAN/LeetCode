class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        l, r = 0, len(piles)-1
        count = 0
        while l < r:
            l += 1
            r -= 1

            if l <= r:
                count += piles[r]
                r -= 1
            else:
                break

        return count