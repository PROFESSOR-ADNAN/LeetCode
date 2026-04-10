class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # position.sort()
        
        # ans = [0] * len(position)
        # ans[0] = 1
        # ans[-1] = 1

        # m -= 2

        # if m == 0:
        #     return position[-1] - position[0]

        # def putMid(left, right):
        #     nonlocal m
        #     mid = left + (right - left) // 2
        #     ans[mid] = 1
        #     m -= 1
        #     if m > 0:
        #         putMid(0, mid-1)

        #     if m > 0:
        #         putMid(mid+1, len(position))

        # putMid(0, len(position))
        # res = float("inf")
        # for i in range(len(position)):
        #     for j in range(i+1, len(position)):
        #         if ans[i] == 1 and ans[j] == 1:
        #             res = min(res, position[j]-position[i])
        
        # print(res)
        # return res
        
        # position.sort()

        # def isValid(val):
        #     ind = 0
        #     cnt = 1
        #     while ind < len(position):
        #         curr = position[ind]
        #         while ind < len(position) and position[ind] - curr != val:
        #             ind += 1

        #         if ind < len(position): 
        #             cnt += 1

        #     return cnt >= m
            
        # left, right = 1, max(position)
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     if isValid(mid):
        #         left = mid + 1
        #     else:
        #         right = mid - 1

        # return right

        position.sort()

        def isValid(val):
            start = float("-inf")
            count = 0
            for p in position:
                if p - start >= val:
                    start = p
                    count += 1

            return count >= m


        left, right = 0, position[-1]
        while left <= right:
            mid = left + (right - left) // 2
            if isValid(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right
