class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        max_len = 0
        fruits_type = {}
        l = 0
        for r in range(len(fruits)):
            fruits_type[fruits[r]] = 1 + fruits_type.get(fruits[r], 0)
            while len(fruits_type) > 2:
                fruits_type[fruits[l]] -= 1
                if fruits_type[fruits[l]] == 0:
                    del fruits_type[fruits[l]]
                l += 1
            max_len = max(max_len, r-l+1)

        return max_len