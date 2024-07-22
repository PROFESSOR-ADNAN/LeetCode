class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """   
        arr = s.split(" ")
        arr.sort(key = lambda x: int(x[-1]))
        return " ".join(x[:-1] for x in arr)