class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        counter = 0
        index = 0
        for i in range(len(g)):
            for j in range(index, len(s)):
                if g[i] <= s[j]:
                    counter += 1
                    index = j+1
                    break
        return counter
        