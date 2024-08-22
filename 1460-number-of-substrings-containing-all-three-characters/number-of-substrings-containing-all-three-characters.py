class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ch = {'a': 0, 'b': 0, 'c': 0}
        cnt = 0
        l, r = 0, 0
        while r < len(s):
            ch[s[r]] = 1 + ch.get(s[r], 0)
            while ch['a'] > 0 and ch['b'] > 0 and ch['c'] > 0:
                cnt += len(s) - r
                ch[s[l]] -= 1
                l += 1
            r += 1

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