class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # countS, countT = Counter(s), Counter(t)
        # operation = 0

        # for key, value in countT.items():
        #     if key in countS:
        #         operation += abs(value - countS[key])
        #     else:
        #         operation -= countT[key]

        # return operation

        # countS, countT = Counter(s), Counter(t)
        # operation = 0

        # for ch in t:
        #     if ch not in countS:
        #         operation += countT[ch]
        #     elif countT[ch] < countS[ch]:
        #         operation += countS[ch] - countT[ch]
        
        # return operation
            

        # countS, countT = Counter(s), Counter(t)
        # operation = 0

        # for ch, freq in countT.items():
        #     if ch in countS and freq > countS[ch]:
        #         operation += freq - countS[ch]

        # return operation


        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1
            count[ord(t[i]) - ord("a")] -= 1
    
        ans = 0
        for val in count:
            if val > 0:
                ans += val  

        return ans















