class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        ch = {}
        l = 0
        r = 0
        while r < len(s):
            if s[r] in ch:
                if ch[s[r]] >= l:
                    l = ch[s[r]] + 1
            ch[s[r]] = r
            max_len = max(max_len, r-l+1)
            r += 1

        return max_len