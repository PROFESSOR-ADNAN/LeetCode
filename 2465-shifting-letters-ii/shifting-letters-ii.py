class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # ans = [0] * len(s)
        # for start, end, shift in shifts:
        #     if shift == 1:
        #         ans[start] += 1
        #         if end + 1 < len(s):
        #             ans[end+1] -= 1
        #     else:
        #         ans[start] -= 1
        #         if end + 1 < len(s):
        #             ans[end+1] += 1

        # for i in range(1, len(ans)):
        #     ans[i] += ans[i-1]

        # for i in range(len(s)):
        #     ch = s[i]
        #     ans[i] = (ans[i] + (ord(ch)-ord("a"))) % 26

        # res = ""
        # for val in ans:
        #     res += chr(val + ord("a"))

        # return res

        Row = len(shifts)
        Col = len(shifts[0])

        n = len(s)
        all_shifts = [0] * n

        for l, r, d in shifts:
            if d:
                all_shifts[l] += 1
                if r+1 < n:
                    all_shifts[r+1] += -1
            else:
                all_shifts[l] += -1
                if r+1 < n:
                    all_shifts[r+1] += 1

        for i in range(1, n):
            all_shifts[i] += all_shifts[i-1]

        ans = []
        for i in range(n):
            ch = s[i]
            shift = all_shifts[i]

            new_ch = chr((((ord(ch)-ord("a"))+shift) % 26) + ord("a"))
            ans.append(new_ch)

        return "".join(ans)






