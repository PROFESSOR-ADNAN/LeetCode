class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        for i in range(len(haystack)-n+1):
            temp = ''
            for j in range(i, i+n):
                temp += haystack[j]
            if temp == needle:
                return i
        return -1











        # l, r = 0, 0
        # s = []
        # while r < len(haystack):
        #     s.append(haystack[r])
        #     while len(s) > len(needle):
        #         s.remove(haystack[l])
        #         l += 1
            
        #     if needle == ''.join(s):
        #         return l
        #     r += 1

        # return -1




        