class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        max_volume = 0
        while l < r:
            max_volume = max(max_volume, ((r-l) * (min(height[l], height[r]))))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_volume


        # l, r = 0, 1
        # max_volume = 0

        # while r < len(height):
        #     max_volume = max(max_volume, ((r-l) * (min(height[l], height[r]))))
        #     if height[r] > height[l]:
        #         l = r
        #     r += 1

        # return max_volume