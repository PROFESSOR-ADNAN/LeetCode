class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        total, running_count = 3, 0
        mpp = {'a': 0, 'b': 0, 'c': 0}
        res = 0
        while r < len(s):
            curr_ch = s[r]
            if mpp[curr_ch] == 0:
                running_count += 1
            mpp[curr_ch] += 1
            while total == running_count:
                res += len(s)-r
                mpp[s[l]] -= 1
                if mpp[s[l]] == 0:
                    running_count -= 1
                l += 1
            r += 1
        
        return res



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