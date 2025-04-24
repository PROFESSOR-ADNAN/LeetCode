class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """   
        arr = list(s.split())
        arr.sort(key = lambda x: x[-1])
        ans = ''
        for word in arr:
            ans += word[:len(word)-1] + " "
        return ans[:len(ans)-1]










        # arr = s.split(" ")
        # arr.sort(key = lambda x: int(x[-1]))
        # return " ".join(x[:-1] for x in arr)