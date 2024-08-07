class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        seen = {}
        for itm in arr:
            if itm in seen:
                seen[itm] += 1
            else:
                seen[itm] = 1
        res = []
        for itm in arr:
            if seen[itm] == 1:
                res.append(itm)
        print(seen)
        print(res)
        return res[k-1] if k > 0 and k <= len(res) else ""
            