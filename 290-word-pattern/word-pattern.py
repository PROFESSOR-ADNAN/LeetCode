class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # words = s.split()
        # unique_words = set(words)

        # return  len(pattern) == len(words) and len(set(pattern)) == len(unique_words)

        words = s.split()

        if len(pattern) != len(words): return False
        letterToWord = {}

        n = len(pattern)
        for i in range(n):
            ch = pattern[i]
            word = words[i]

            if ch in letterToWord:
                if word != letterToWord[ch]:
                    return False
            elif word in letterToWord.values():
                return False
            else:
                letterToWord[ch] = word

        return True
            