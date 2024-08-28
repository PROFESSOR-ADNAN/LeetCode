class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)):
            s = ""
            for j in range(i, len(haystack)):
                s += haystack[j]
                if s == needle:
                    return i
                elif len(s) > len(needle):
                    break
                    
        return -1


        