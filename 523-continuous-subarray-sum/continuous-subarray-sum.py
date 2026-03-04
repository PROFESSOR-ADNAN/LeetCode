class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # left = 0
        # curr_sum = 0
        # for right in range(len(nums)):
        #     curr_sum += nums[right]

        #     if curr_sum % k == 0 and (right-left+1 >= 2):
        #         return True

            
        # for i in range(len(nums)):
        #     curr_sum = 0
        #     for j in range(i, len(nums)):
        #         curr_sum += nums[j]
        #         if curr_sum % k == 0 and (j-i+1 >= 2):
        #             return True

        # return False

        # prefix = []
        # for i in range(len(nums)):
        #     if i > 0:
        #         nums[i] += nums[i-1]
        #     prefix.append(nums[i]%k)
        # print(nums)
        # print(prefix)
        # mpp = {}
        # for i in range(len(prefix)):
        #     if prefix[i] in mpp and i - mpp[prefix[i]] + 1 >= 2:
        #         return True

        #     mpp[prefix[i]] = i

        # return True if 0 in prefix else False

        # if len(nums) < 2:
        #     return False

        # for i in range(2, len(nums)+1):
        #     m = i
        #     for j in range(len(nums)+1-m):
        #         sum_ = 0
        #         for n in range(j, m+j):
        #             sum_ += nums[n]

        #         print(sum_)
        #         if sum_ % k == 0:
        #             return True

        # return False

        # mpp = {0: -1}
        # curr = 0
        # for i in range(len(nums)):
        #     curr += nums[i]
        #     r = curr % k
        #     if r in mpp and i-mpp[r] >= 2:
        #         return True
        #     if r in mpp:
        #         mpp[r] = min(i, mpp[r])

        # return False


        mpp = {0: -1}
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            r = curr % k
            # if r in mpp and i-mpp[r] >= 2:
            #     return True
            # if r in mpp:
            #     mpp[r] = min(i, mpp[r])

            if r not in mpp:
                mpp[r] = i
            elif i - mpp[r] > 1:
                return True

        return False

        return False
