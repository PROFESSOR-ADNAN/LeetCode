class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ans = [0] * len(s)
        for start, end, shift in shifts:
            if shift == 1:
                ans[start] += 1
                if end + 1 < len(s):
                    ans[end+1] -= 1
            else:
                ans[start] -= 1
                if end + 1 < len(s):
                    ans[end+1] += 1

        for i in range(1, len(ans)):
            ans[i] += ans[i-1]

        for i in range(len(s)):
            ch = s[i]
            ans[i] = (ans[i] + (ord(ch)-ord("a"))) % 26

        res = ""
        for val in ans:
            res += chr(val + ord("a"))

        return res