class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict(int)
        for ind, num in enumerate(nums):
            diff = target - num
            if diff in map:
                return [map[diff], ind]
            map[num] = ind