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
            if people[r] < limit and people[l] <= limit - people[r]:
                l += 1
            boats += 1
            r -= 1

        return boats