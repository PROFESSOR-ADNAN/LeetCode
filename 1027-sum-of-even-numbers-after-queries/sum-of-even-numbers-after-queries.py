class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # answer = []
        # for val, ind in queries:
        #     nums[ind] += val
        #     sum_ = 0
        #     for num in nums:
        #         if num % 2 == 0:
        #             sum_ += num

        #     answer.append(sum_)

        # return answer

        answer = []
        ini_sum = 0
        for num in nums:
            if num % 2 == 0:
                ini_sum += num
        
        for val, ind in queries:
            if nums[ind] % 2 == 0:
                ini_sum -= nums[ind]

            nums[ind] += val

            if nums[ind] % 2 == 0:
                ini_sum += nums[ind] 
            
            
            answer.append(ini_sum)

        return answer