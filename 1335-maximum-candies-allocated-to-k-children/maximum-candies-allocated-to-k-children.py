class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # if k > len(candies):
        #     return 0

        # return min(candies)

        def isPoss(val):
            childs = 0
            for candie in candies:
                childs += candie // val

            return childs >= k

        left, right = 1, max(candies)
        while left <= right:
            mid = left + (right - left) // 2
            if isPoss(mid):
                left = mid + 1
            else:
                right = mid - 1

            print(left, right, mid)
        
        return right