class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        count = OrderedDict()
        for ch in arr:
            count[ch] = count.get(ch, 0) + 1
        print(count)
        res = []
        for ch, cnt in count.items():
            if cnt  == 1:
                res.append(ch)
        print(res)
        return res[k-1] if k <= len(res) else ""