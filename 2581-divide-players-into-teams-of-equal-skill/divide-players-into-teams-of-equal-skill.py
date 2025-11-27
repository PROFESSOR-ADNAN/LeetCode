class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        total = sum(skill)
        target = total // (len(skill)/2)

        count = Counter(skill)
        chemistry = 0

        for c in skill:
            if not count[c]:
                continue
            count[c] -= 1
            if not count[target-c]:
                return -1
            count[target-c] -= 1

            chemistry += (c * (target-c))
        return chemistry


        # skill.sort()
        # l, r = 0, len(skill)-1
        # initial_val = skill[l] + skill[r]
        # chemistry = 0

        # while l < r:
        #     if skill[l] + skill[r] != initial_val:
        #         return -1
        #     chemistry += (skill[l] * skill[r])
        #     l += 1
        #     r -= 1

        # return chemistry




        # skill.sort()
        # l, r = 0, len(skill)-1

        # res = []
        # while l < r:
        #     res.append((skill[l], skill[r]))
        #     l += 1
        #     r -= 1
        
        # val = res[0][0] + res[0][1]
        # chemistry = 0
        # for a1, a2 in res:
        #     if a1 + a2 != val:
        #         return -1
        #     chemistry += (a1 * a2)
        
        # return chemistry
