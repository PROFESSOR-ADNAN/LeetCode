class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ''
        for c in digits:
            num += str(c)
        num = str(int(num) + 1)
        ans = list(num)
        for i in range(len(ans)):
            ans[i] = int(ans[i])
        return ans
            

