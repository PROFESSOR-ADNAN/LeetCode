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
            if s[r] in ch:
                ch.remove(s[l])
                l += 1
            if s[r] not in ch:
                ch.add(s[r])
                max_len = max(max_len, r-l+1)
                r += 1
            

        return max_len