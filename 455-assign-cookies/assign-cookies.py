class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i, j = 0, 0
        count = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return count











        # g.sort()
        # s.sort()
        # i = 0
        # j = 0
        # while j < len(s):
        #     if i < len(g) and s[j] >= g[i]:
        #         i += 1
        #     j += 1
        # return i
                