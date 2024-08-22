class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        s = str(num)
        s = list(s)
        cnt = 0
        x = []
        l = 0
        for r in range(len(s)):
            x.append(s[r])

            if len(x) == k:
                if int(''.join(x)) != 0 and num % int(''.join(x)) == 0:
                    cnt += 1
                x.remove(s[l])
                l += 1
        
        return cnt
            
                



            


        