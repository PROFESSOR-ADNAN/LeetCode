class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # ans = []
        # n = len(nums)
        # count = Counter(nums)
        # for num, cnt in count.items():
        #     if cnt > n // 3:
        #         ans.append(num) 

        # return ans

        # cnt = len(nums)//3

        # count = Counter(nums)

        # ans = []
        # for key, value in count.items():
        #     if value > cnt:
        #         ans.append(key)
            
        # return ans
        # n = len(nums)-1

        # c1, cnt1 = nums[0], 1
        # c2, cnt2 = nums[n-1], 1

        # for i in range(1,n-1):
        #     curr_front = nums[i]
        #     curr_back = nums[n-i]
        #     if curr_front == c1:
        #         cnt1 += 1
        #     else:
        #         cnt1 -= 1

        #     if curr_back == c2:
        #         cnt2 += 1
        #     else:
        #         cnt2 -= 1
            
        #     if cnt1 == 0:
        #         c1 = curr

        #     if cnt2 == 0:
        #         c2 = cur

        # print(c1, c2)
        # return []



        # n = len(nums)
        # ans = []

        # if cnt1 > n//3:
        #     ans.append(cand1)
        
        # if cnt2 > n//3:
        #     ans.append(cand2)

        # return ans


        cand1, cand2 = 0, 0
        cnt1, cnt2 = 0, 0

        for num in nums:
            if (cnt1 and cnt2) or cand1 == num or cand2 == num:
                if num == cand1:
                    cnt1 += 1
                elif num == cand2:
                    cnt2 += 1
                else:
                    cnt1 -= 1
                    cnt2 -= 1
            else:
                if cnt1 == 0:
                    cand1 = num
                    cnt1 += 1
                else:
                    cand2 = num
                    cnt2 += 1

        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == cand1:
                cnt1 += 1
            elif num == cand2:
                cnt2 += 1
        
        n = len(nums)
        ans = []
        if cnt1 > n//3:
            ans.append(cand1)
        if cnt2 > n//3:
            ans.append(cand2)

        return ans







