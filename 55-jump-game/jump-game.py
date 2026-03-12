class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # if 0 == len(nums)-1: return True

        # ind = 0
        # while ind < len(nums):
        #     ind += nums[ind]

        #     if ind == len(nums)-1:
        #         return True
        #     elif ind < len(nums) and nums[ind] == 0:
        #         return False
        #     elif ind > len(nums)-1 and nums[len(nums)-1] == 0:
        #         return True

        # return False


        furthest = 0
        for i in range(len(nums)):
            if i > furthest:
                return False

            furthest = max(furthest, i + nums[i])

        return True