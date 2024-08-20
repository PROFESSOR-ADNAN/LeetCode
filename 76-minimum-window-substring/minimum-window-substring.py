class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        min_len = 1000000000
        s_ind = -1
        ch = Counter(t)
        cnt = 0
        l = 0
        r = 0
        while r < len(s):
            if s[r] in ch and ch[s[r]] > 0:
                cnt += 1
            ch[s[r]] = -1 + ch.get(s[r], 0)
            while cnt == len(t):
                if (r-l+1) < min_len:
                    min_len = (r-l+1)
                    s_ind = l
                ch[s[l]] += 1
                if ch[s[l]] > 0:
                    cnt -= 1
                l += 1
            r += 1

        return s[s_ind:s_ind+min_len] if s_ind != -1 else ""

        