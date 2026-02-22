class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # left, right = 0, num
        # while left + 1 < right:
        #     mid = (left + right)//2
        #     a, b, c = mid-1, mid, mid+1
        #     if a+b+c == num:
        #         return [a,b,c]
        #     elif a+b+c > num:
        #         right = mid
        #     else:
        #         left = mid


        # return []        

        # a, b, c = -1, 0, 1
        # while c < num + 2:
        #     if a + b + c == num:
        #         return [a, b, c]
        #     a += 1
        #     b += 1
        #     c += 1

        # return []

        left, right = -1, num+1
        while left + 1< right:
            mid = (left + right)//2
            a, b, c = mid-1, mid, mid+1
            if a+b+c == num:
                return [a,b,c]
            elif a+b+c > num:
                right = mid
            else:
                left = mid

        return []