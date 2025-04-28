class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l, r = 0, 0
        count = {}
        maxL = 0
        maxF = 0
        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])
            if (r-l+1) - maxF > k:
                count[s[l]] -= 1
                l += 1
            if (r-l+1) - maxF <= k:
                maxL = max(maxL, r-l+1)
            r += 1
        
        return maxL





        # l, r = 0, 0
        # maxL = 0
        # maxF = 0
        # count = {}
        # while r < len(s):
        #     count[s[r]] = 1 + count.get(s[r], 0)
        #     for value in count.values():
        #         maxF = max(maxF, value)
        #     while (r-l+1) - maxF > k:
        #         count[s[l]] -= 1
        #         l += 1
        #     for value in count.values():
        #         maxF = max(maxF, value)
            
        #     maxL = max(maxL, r-l+1)
        #     r += 1
        
        # return maxL
            




        # maxL = 0
        # for i in range(len(s)):
        #     count = {}
        #     for j in range(i, len(s)):
        #         count[s[j]] = 1 + count.get(s[j], 0)
                
        #         highest = 0
        #         for key, value in count.items():
        #             if value > highest:
        #                 highest = value
                
        #         if (j-i+1) - highest <= k:
        #             maxL = max(maxL, j-i+1)

        # return maxL





        # max_len = 0
        # max_f = 0
        # ch = {}
        # l, r = 0, 0
        # while r < len(s):
        #     ch[s[r]] = 1 + ch.get(s[r], 0)
        #     max_f = max(max_f, ch[s[r]])
        #     if (r-l+1) - max_f > k:
        #         ch[s[l]] -= 1
        #         l += 1
        #     if (r-l+1) - max_f <= k:
        #         max_len = max(max_len, (r-l+1))
        #     r += 1
        
        # return max_len


        # # l, r = 0, 0
        # # substring = ""
        # # max_len = 0
        # # while r < len(s):
        # #     substring += s[r]
        # #     if len(substring) > k+1:
        # #         count = {}
        # #         count = Counter(substring)
        # #         for key, cnt in count.items():
        # #             if cnt == len(substring) - k:
        # #                 max_len = max(max_len, r-l+1)
        # #                 break
        # #     r += 1
    
        # # return max_len
