class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        ch = set()
        l = 0
        r = 0
        while r < len(s):
            while s[r] in ch:
                ch.remove(s[l])
                l += 1
            max_len = max(max_len, r-l+1)
            ch.add(s[r])
            r += 1
        
        return max_len