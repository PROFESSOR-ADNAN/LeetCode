class Solution:
    def removeStars(self, s: str) -> str:
        newS = []
        cnt = 0
        for ch in s[::-1]:
            if ch != "*":
                if cnt == 0:
                    newS.append(ch)
                else:
                    cnt -= 1
            else:
                cnt += 1

        return "".join(newS[::-1])
