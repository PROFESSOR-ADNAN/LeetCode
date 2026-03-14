class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # left = 0
        # cnt  = 0
        # prefix = nums.copy()
        # suffix = nums.copy()
        # prefixSet = set([0])
        # suffixSet = set([0])

        # for i in range(1, n):
        #     prefix[i] += prefix[i-1]

        # for i in range(n-2, -1, -1):
        #     suffix[i] += suffix[i+1]
        
        # suffix.reverse()

        # for num in prefix:
        #     if num < k:
        #         if k % num in prefixSet:
        #             cnt += 1
        #     else:
        #         if num % k in prefixSet:
        #             cnt += 1
        #     prefixSet.add(abs(num))


        # print(suffix)
        # for num in suffix:
        #     # if num < k:
        #     #     if k % num in suffixSet:
        #     #         cnt += 1
        #     #     print(k % num)
        #     # else:
        #     if num % k in suffixSet:
        #         cnt += 1
        #     print(num % k)

        #     suffixSet.add(abs(num))
        #     print(num, suffixSet, cnt)

        # return cnt
 
        # reminders = defaultdict(int)
        # reminders[0] += 1
        # count = 0
        # curr = 0

        # for num in nums:
        #     curr += num
        #     rem = curr % k
        #     if rem in reminders:
        #         count += reminders[rem]
            
        #     reminders[rem] += 1

        # return count

        mpp = defaultdict(int)
        mpp[0] += 1
        cnt = 0
        curr = 0
        
        for num in nums:
            curr += num
            reminder = curr % k
            if reminder in mpp:
                cnt += mpp[reminder]
            mpp[reminder] += 1

        return cnt









