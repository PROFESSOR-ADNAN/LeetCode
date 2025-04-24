class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = list(s)
        vowels = []
        ind = []
        for i in range(len(s)):
            if arr[i] in "aeiouAEIOU":
                vowels.append(arr[i])
                ind.append(i)

        vowels.sort()
        for i in range(len(vowels)):
            arr[ind[i]] = vowels[i]

        return ''.join(arr)













        # vowel = "AEIOUaeiou"
        # vowels = [char for char in s if char in vowel]
        # vowels_sorted = sorted(vowels)
        # res = ""
        # j = 0
        # for i in range(len(s)):
        #     if s[i] in vowel:
        #         res += vowels_sorted[j]
        #         j += 1
        #     else:
        #         res += s[i]
        # return res
                