class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        sorting_map = {}
        word = ""
        res = ""
        count = 1

        s += " "
        for letter in s:
            if letter == " ":
                num = int(word[-1])
                sorting_map[num] = word[:-1:]
                word = ""
                letter = ""
                count += 1
            word += letter
        for i in range(1, count):
            res += sorting_map[i]
            if count != i + 1:
                res += " "
        
        return res