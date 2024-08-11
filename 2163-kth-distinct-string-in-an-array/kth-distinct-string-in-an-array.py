class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        count = Counter(arr)
        for ch in arr:
            if count[ch] == 1:
                k -= 1
                if k == 0:
                    return ch
        return ""

