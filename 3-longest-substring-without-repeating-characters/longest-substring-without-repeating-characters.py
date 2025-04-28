class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxCount = 0
        for i in range(len(s)):
            count = 0
            unique = set()
            for j in range(i, len(s)):
                if s[j] not in unique:
                    unique.add(s[j])
                    count += 1
                else:
                    break
            maxCount = max(maxCount, count)

        return maxCount




        # max_len = 0
        # ch = {}
        # l = 0
        # r = 0
        # while r < len(s):
        #     if s[r] in ch:
        #         if ch[s[r]] >= l:
        #             l = ch[s[r]] + 1
        #     max_len = max(max_len, r-l+1)
        #     ch[s[r]] = r
        #     r += 1

        # return max_len