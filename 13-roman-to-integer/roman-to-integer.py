class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanToInt = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        num = 0
        for i in range(len(s)):
            if s[i] == "I":
                if i+1 < len(s) and (s[i+1] == "V" or s[i+1] == "X"):
                    num -= romanToInt[s[i]]
                else:
                    num += romanToInt[s[i]]
            elif s[i] == "X":
                if i+1 < len(s) and (s[i+1] == "L" or s[i+1] == "C"):
                    num -= romanToInt[s[i]]
                else: 
                    num += romanToInt[s[i]]
            elif s[i] == "C":
                if i+1 < len(s) and (s[i+1] == "D" or s[i+1] == "M"):
                    num -= romanToInt[s[i]]
                else:
                    num += romanToInt[s[i]]
            else:
                num += romanToInt[s[i]]

        return num