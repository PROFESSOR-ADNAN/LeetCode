class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        firstRow = set("qwertyuiop")
        secondRow = set("asdfghjkl")
        thirdRow = set("zxcvbnm")
        
        def helper(word, row):
            for c in word:
                if c.lower() not in row:
                    return False
            return True

        ans = []
        for word in words:
            if helper(word, firstRow):
                ans.append(word)
            if helper(word, secondRow):
                ans.append(word)
            if helper(word, thirdRow):
                ans.append(word)

        return ans
