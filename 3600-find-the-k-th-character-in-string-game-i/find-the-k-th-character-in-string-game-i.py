class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        word = "a"
        def append(word):
            if len(word) >= k:
                return word[k-1]
            generated = ""
            for c in word:
                generated += chr(ord(c) + 1)
                print(generated)
            return append(word + generated)

        return append(word)
        