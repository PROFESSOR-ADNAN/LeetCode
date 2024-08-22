class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        ch = {}

        for r in range(len(s)):
            ch[s[r]] = r
            if len(ch) == 3:
                cnt += 1 + min(ch['a'], ch['b'], ch['c'])
        
        return cnt















        # l, r = 0, 0
        # total_len = 0
        # letters = {"a", "b", "c"}
        # while r < len(s):
        #     if s[r] in letters:
        #         letters.remove(s[r])
        #     if not letters:
        #         total_len += len(s) - r
        #         l += 1
        #         r = l - 1
        #         letters = {"a", "b", "c"}
        #     r += 1

        # return total_len