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
        print(seen)
        count = []
        for key in seen:
            count.append([seen[key], key])
        print(count)
        count.sort()
        print(count)
        res = []
        for i in range(len(count)-1, len(count)-k-1, -1):
            res.append(count[i][1])
        print(res)
        return res

        
     
        