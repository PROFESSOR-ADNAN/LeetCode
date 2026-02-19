class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        count = Counter(nums)
        for num, cnt in count.items():
            if cnt > n // 3:
                ans.append(num) 

        return ans