class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # if len(word1) != len(word2):
        #     return False

        # return not (set(word1)-set(word2))

        if len(word1) != len(word2) or set(word1) - set(word2):
            return False

        if not word1:
            return True

        cnt_word1 = Counter(word1)
        cnt_word2 = Counter(word2)

        freq1 = sorted(list(cnt_word1.values()))
        freq2 = sorted(list(cnt_word2.values()))

        if freq1 == freq2:
            return True 
        
        return False