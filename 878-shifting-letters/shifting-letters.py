class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        for i in range(len(shifts)-2, -1, -1):
            shifts[i] += shifts[i+1]

        newStr = ""
        for i in range(len(s)):
            newStr += chr(((ord(s[i])-ord("a") + shifts[i]) % 26) + ord("a"))

        return newStr