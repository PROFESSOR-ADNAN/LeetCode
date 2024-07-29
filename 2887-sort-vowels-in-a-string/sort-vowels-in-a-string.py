class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel_in_the_string = []
        vowels = "aeiouAEIOU"
        for i in range(len(s)):
            if s[i] in vowels:
                vowel_in_the_string.append(s[i])
        vowels_sorted = sorted(vowel_in_the_string)
        ans = ""
        j = 0
        for i in range(len(s)):
            if s[i] in vowels:
                ans += vowels_sorted[j]
                j += 1
            else:
                ans += s[i]
        return ans
                