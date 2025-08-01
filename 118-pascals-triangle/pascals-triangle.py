class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[1]]
        for _ in range(numRows - 1):
            arr = []
            l, r = -1, 0
            while len(arr) != len(ans[-1]) + 1:
                left = ans[-1][l] if l >= 0 else 0
                right = ans[-1][r] if r < len(ans[-1]) else 0
                arr.append(left + right)
                l += 1
                r += 1
            ans.append(arr)
        return ans
        