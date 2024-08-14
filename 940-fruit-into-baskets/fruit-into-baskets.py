class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        fruit_type = set()
        l, r = 0, 0
        max_len = 0
        while r < len(fruits):
            if len(fruit_type) < 2 and fruits[r] not in fruit_type:
                fruit_type.add(fruits[r])
                max_len = max(max_len, r-l+1)
            elif fruits[r] in fruit_type:
                max_len = max(max_len, r-l+1)
            else:
                fruit_type = set()
                fruit_type.add(fruits[r-1])
                fruit_type.add(fruits[r])
                l = r-1
                
                while fruits[l] == fruits[l-1]:
                    l -= 1
            r += 1

        return max_len