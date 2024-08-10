class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        res = []
        for key in seen:
            res.append((seen[key], key))
        res.sort()
        ans = []
        for i in range(len(res)-1, len(res)-k-1, -1):
            ans.append(res[i][1])

        return ans