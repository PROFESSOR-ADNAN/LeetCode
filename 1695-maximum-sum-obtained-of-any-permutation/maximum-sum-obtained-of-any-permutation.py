class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # n = len(nums)
        # prefix = [0] * n

        # for i in range(len(requests)):
        #     start = requests[i][0]
        #     end = requests[i][1]

        #     prefix[start] += 1
        #     if end + 1 < n:
        #         prefix[end+1] -= 1

        # for i in range(1, n):
        #     prefix[i] += prefix[i-1]

        # prefixCount = sorted([[key, cnt] for key, cnt in Counter(prefix).items()], reverse=True)
        # nums.sort(reverse=True)
        # ind = 0

        # prefixToNum = defaultdict(list)
        # for key, cnt in prefixCount:
        #     for _ in range(cnt):
        #         prefixToNum[key].append(nums[ind])
        #         ind += 1


        # for i in range(n):
        #     val = prefix[i]
        #     prefix[i] = prefixToNum[val].pop()

        # for i in range(1, n):
        #     prefix[i] += prefix[i-1]

        # ans = 0
        # for start, end in requests:
        #     if start > 0:
        #         ans += prefix[end]-prefix[start-1]
        #     else:
        #         ans += prefix[end]

        # return ans % (10**9 + 7)

        MOD = 10 ** 9 + 7
        n = len(nums)
        prefix = [0] * n

        for start, end in requests:
            prefix[start] += 1
            if end + 1 < n:
                prefix[end + 1] -= 1

        for i in range(1, n):
            prefix[i] += prefix[i-1]

        prefix.sort()
        nums.sort()
        ans = 0

        for i in range(n):
            ans += prefix[i] * nums[i]

        return ans % MOD