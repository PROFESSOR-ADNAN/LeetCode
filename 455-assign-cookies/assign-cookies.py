class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = 0
        j = 0
        while j < len(s):
            if i < len(g) and s[j] >= g[i]:
                i += 1
            j += 1
        return i
                