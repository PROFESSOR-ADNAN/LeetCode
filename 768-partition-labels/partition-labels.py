class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        count = Counter(s)
        l = 0
        ans = []

        for r in range(len(s)):
            count[s[r]] -= 1
            if not count[s[r]]:
                for letter in set(s[l:r]):
                    if count[letter]:
                        break
                else:
                    ans.append(r-l+1)
                    l = r+1
        return ans