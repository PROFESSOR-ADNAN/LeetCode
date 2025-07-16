class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        parities = [num % 2 for num in nums]

        last = None
        alt_No = 0
        for p in parities:
            if last is None or p != last:
                alt_No += 1
                last = p

        count_even = parities.count(0)
        count_odd = parities.count(1)
        same_parity = max(count_even, count_odd)

        return max(same_parity, alt_No)
        