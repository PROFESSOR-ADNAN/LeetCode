class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        temp = [0] * (len(s) + 1)
        for l, r, k in shifts:
            if k == 1:
                temp[l] += 1
                temp[r+1] -= 1
            else:
                temp[l] -= 1
                temp[r+1] += 1

        for i in range(1, len(temp)):
            temp[i] += temp[i-1]
        newStr = ""
        for i in range(len(s)):
            newStr += chr(((ord(s[i]) - ord("a") + temp[i]) % 26) + ord("a"))

        return newStr



        # asciiS = [ord(char) for char in s]
        # temp = [0] * len(s)

        # for l, r, k in shifts:
        #     if k == 0:
        #         temp[l] += -1
        #         if r+1 < len(temp):
        #             temp[r+1] += 1
        #     else:
        #         temp[l] += 1
        #         if r+1 < len(temp):
        #             temp[r+1] += -1

        # for i in range(1, len(temp)):
        #     temp[i] += temp[i-1]

        # for i in range(len(temp)):
        #     res = asciiS[i] + temp[i]
        #     if res < ord("a"):
        #         res = ord("z") - (ord("a")-res) + 1
        #     elif res > ord("z"):
        #         res = ord("a") + (res-ord("z")) - 1
        #     asciiS[i] = res


        # ans = ""
        # for i in range(len(asciiS)):
        #     ans += chr(asciiS[i])

        # return ans
            


#         temp = [0] * (len(s) + 1)
#         for st, e, d in shifts:
#             if d:
#                 temp[st] += 1
#                 temp[e+1] -= 1
#             else:
#                 temp[st] -= 1
#                 temp[e+1] += 1
#         for i in range(1, len(temp)):
#             temp[i] += temp[i-1]
        
#         new_s = ''
#         for i in range(len(s)):
#             new_s += chr(((ord(s[i]) - ord('a') + temp[i]) % 26 ) + ord('a')
# )
#         return new_s
        