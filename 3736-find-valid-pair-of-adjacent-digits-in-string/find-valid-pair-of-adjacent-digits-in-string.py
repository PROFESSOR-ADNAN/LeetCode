class Solution:
    def findValidPair(self, s: str) -> str:
        count_s = Counter(s)
        for i in range(1, len(s)):
            if s[i-1] != s[i] and count_s[s[i-1]] == int(s[i-1]) and count_s[s[i]] == int(s[i]):
                return s[i-1:i+1]

        return ""