class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def is_len_above_3(s):
            return True if len(s) >= 3 else False
        
        def is_letter(c):
            if (ord("a") <= ord(c) <= ord("z") or
                ord("A") <= ord(c) <= ord("Z")):
                return True
            return False

        def is_number(c):
            if ord("0") <= ord(c) <= ord("9"):
                return True
            return False

        def is_alpha_numeric(s):
            for c in s:
                if not (is_letter(c) or is_number(c)):
                    return False
            return True


        def has_vowel(s):
            for c in s:
                if is_letter(c) and c in "aeiouAEIOU":
                    return True
            return False

        def has_consonant(s):
            for c in s:
                if is_letter(c) and c not in "aeiouAEIOU":
                    return True
            return False

        return (is_len_above_3(word) and is_alpha_numeric(word) and has_vowel(word) and has_consonant(word))


