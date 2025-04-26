class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def isPalindromic(num):
            l, r = 0, len(num)-1
            while l < r:
                if num[l] != num[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i in range(2, n-1):
            curr = n
            currStr = ''
            while curr:
                r = curr % i
                curr = curr // i
                currStr += str(r)

            if not isPalindromic(currStr):
                return False

        return True