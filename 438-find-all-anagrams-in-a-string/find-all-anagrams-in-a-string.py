class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ans = []
        countP = Counter(p)
        countS = Counter(s[:len(p)])
        if countP == countS:
            ans.append(0)
        for r in range(len(p), len(s)):
            countS[s[r-len(p)]] -= 1
            if countS[s[r-len(p)]] == 0:
                del countS[s[r-len(p)]]
            countS[s[r]] = countS.get(s[r], 0) + 1

            if countP == countS:
                ans.append(r-len(p)+1)
            
        return ans




        # ans = []
        # countP = Counter(p)
        # for i in range(len(s)-len(p)+1):
        #     if countP == Counter(s[i:i+len(p)]):
        #         ans.append(i)

        # return ans
        
        
        
        # ans = []
        # for i in range(len(s)-len(p) + 1):
        #     sub_string = s[i:i+len(p)]
        #     if sorted(p) == sorted(sub_string):
        #         ans.append(i)
        
        # return ans

        