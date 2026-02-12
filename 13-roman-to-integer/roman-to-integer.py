class Solution:
    def romanToInt(self, s: str) -> int:
        romanToInteger = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        integer = 0

        for i in range(len(s)):
            roman_symbol = s[i]
            if roman_symbol == "I":
                if i+1 < len(s) and (s[i+1] == "V" or s[i+1] == "X"):
                    integer -= romanToInteger[roman_symbol]
                else:
                    integer += romanToInteger[roman_symbol]
            elif roman_symbol == "X":
                if i+1 < len(s) and (s[i+1] == "L" or s[i+1] == "C"):
                    integer -= romanToInteger[roman_symbol]
                else:
                    integer += romanToInteger[roman_symbol]
            elif roman_symbol == "C":
                if i+1 < len(s) and (s[i+1] == "D" or s[i+1] == "M"):
                    integer -= romanToInteger[roman_symbol]
                else:
                    integer += romanToInteger[roman_symbol]
            else:
                integer += romanToInteger[roman_symbol]

        return integer
            