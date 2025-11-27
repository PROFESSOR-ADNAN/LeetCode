class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        l, r = 0, len(skill)-1

        res = []
        while l < r:
            res.append((skill[l], skill[r]))
            l += 1
            r -= 1
        
        val = res[0][0] + res[0][1]
        chemistry = 0
        for a1, a2 in res:
            if a1 + a2 != val:
                return -1
            chemistry += (a1 * a2)
        
        return chemistry
