class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        res = []
        for i in range(len(arr)):
            condition = False
            for j in range(len(arr)):
                if i != j and arr[j] == arr[i]:
                    condition = True
            if not condition:
                res.append(arr[i])
        print(res)
        return res[k-1] if k <= len(res) else ""


