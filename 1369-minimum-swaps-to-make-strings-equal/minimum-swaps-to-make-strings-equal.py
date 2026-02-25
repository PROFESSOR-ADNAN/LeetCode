class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # countBoth = Counter(s1+s2)
        # countS1 = Counter(s1)
        # countS2 = Counter(s2)

        # cntX = countBoth["x"]
        # cntY = countBoth["y"]

        # if cntX % 2 or cntY % 2:
        #     return -1

        # print(cntX, cntY, countBoth.values(), )
        # if cntX == countS1["x"] or cntX == countS2["y"]:
        #     return cntX // 2
        # else:
        #     return min(cntX, cntY)

        # return -1


        count = Counter(s1 + s2)
        if count["x"] % 2 or count["y"] % 2:
            return -1

        mpp = defaultdict(int)

        for a, b in zip(s1, s2):
            if a != b:
                mpp[a+b] += 1

        ans = 0
        for val in mpp.values():
            ans += val // 2 + 1 if val % 2 else val // 2

        return ans