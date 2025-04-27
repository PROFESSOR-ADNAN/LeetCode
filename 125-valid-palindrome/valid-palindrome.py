class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # def isAlphanumeric(s):
        #     if (ord(s) in range(ord('0'), ord('9')+1) or
        #         ord(s) in range(ord('A'), ord('Z')+1) or
        #         ord(s) in range(ord('a'), ord('z')+1)):
        #         return True
        #     return False

        l, r = 0, len(s)-1
        while l < r:
            while l < r and s[l].isalnum() == False:
                l += 1
            while l < r and s[r].isalnum() == False:
                r -= 1
            print(s[l], s[r])
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True






        # def isPalindrome(s):
        #     l, r = 0, len(s)-1
        #     while l < r:
        #         if s[l] != s[r]:
        #             return False
        #         l += 1
        #         r -= 1
        #     return True
        # newS = ''
        # for i in range(len(s)):
        #     if (ord(s[i]) in range(ord('0'), ord('9')+1) or
        #         ord(s[i]) in range(ord('A'), ord('Z')+1) or
        #         ord(s[i]) in range(ord('a'), ord('z')+1)):
        #         newS += s[i].lower()

        # return isPalindrome(newS)





        # only_alphanumeric = []
        # for elem in s.lower().replace(" ", ""):
        #     if (ord(elem) >= 65 and ord(elem) <= 90) or (ord(elem) >= 97 and ord(elem) <= 122):
        #         only_alphanumeric.append(elem)
        # left = 0
        # right = len(only_alphanumeric) - 1
        # while left <= right:
        #     if only_alphanumeric[left] != only_alphanumeric[right]:
        #         return False
        #     else:
        #         left += 1
        #         right -= 1
        # return True
        