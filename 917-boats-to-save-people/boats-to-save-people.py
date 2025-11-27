class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        boats = 0
        l, r = 0, len(people)-1
        while l <= r:
            if l < r and people[r] < limit and people[l] <= limit - people[r]:
                boats += 1
                r -= 1
                l += 1
            else:
                boats += 1
                r -= 1

        return boats