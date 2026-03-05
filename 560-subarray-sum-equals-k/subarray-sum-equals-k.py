class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix = [0]
        # for i in range(len(nums)):
        #     prefix.append(prefix[i]+nums[i])

        # count = 0
        # for i in range(1, len(prefix)):
        #     j = i-1
        #     while j >= 0:
        #         if prefix[i] - prefix[j] == k:
        #             count += 1
        #         j -= 1

        # return count


        # prefix = [0]
        # for i in range(len(nums)):
        #     prefix.append(prefix[i]+nums[i])

        # count = 0
        # for i in range(1, len(prefix)):
        #     j = i-1
        #     while j >= 0:
        #         if prefix[i] - prefix[j] == k:
        #             count += 1
        #         j -= 1

        # return count

        # cnt = 0
        # for i in range(len(nums)):
        #     curr = 0
        #     for j in range(i, len(nums)):
        #         curr += nums[j]
        #         if curr == k:
        #             cnt += 1
        
        # return cnt

        prefix = defaultdict(int)
        prefix[0] = 1
        total = 0
        ans = 0

        for i in range(len(nums)):
            total += nums[i]
            if total - k in prefix:
                ans += prefix[total - k]
            prefix[total] += 1

        return ans


