class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        temp = [0] * (len(s) + 1)
        for st, e, d in shifts:
            if d:
                temp[st] += 1
                temp[e+1] -= 1
            else:
                temp[st] -= 1
                temp[e+1] += 1
        for i in range(1, len(temp)):
            temp[i] += temp[i-1]
        
        new_s = ''
        for i in range(len(s)):
            new_s += chr(((ord(s[i]) - ord('a') + temp[i]) % 26 ) + ord('a')
)
        return new_s
        