class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        l = r = 0
        seen = set()
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            if s[r] not in seen:
                seen.add(s[r])
                max_len = max(max_len, r-l+1)
            r += 1

        return max_len
