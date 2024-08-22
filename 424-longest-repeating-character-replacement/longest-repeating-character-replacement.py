class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_len = 0
        max_f = 0
        ch = {}
        l, r = 0, 0
        while r < len(s):
            ch[s[r]] = 1 + ch.get(s[r], 0)
            max_f = max(max_f, ch[s[r]])
            if (r-l+1) - max_f > k:
                ch[s[l]] -= 1
                l += 1
            if (r-l+1) - max_f <= k:
                max_len = max(max_len, (r-l+1))
            r += 1
        
        return max_len


















        # l, r = 0, 0
        # substring = ""
        # max_len = 0
        # while r < len(s):
        #     substring += s[r]
        #     if len(substring) > k+1:
        #         count = {}
        #         count = Counter(substring)
        #         for key, cnt in count.items():
        #             if cnt == len(substring) - k:
        #                 max_len = max(max_len, r-l+1)
        #                 break
        #     r += 1
    
        # return max_len
