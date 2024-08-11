class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        for i in range(len(arr)):
            distnict_flag = True
            for j in range(len(arr)):
                if i == j:
                    continue
                if arr[i] == arr[j]:
                    distnict_flag = False
            if distnict_flag:
                k -= 1
                if k == 0:
                    return arr[i]
        return ""

