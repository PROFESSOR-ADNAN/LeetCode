class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window = sum(nums[:k])
        max_sum = window
        l = 0
        for r in range(k, len(nums)):
            window -= nums[l]
            window += nums[r]
            
            max_sum = max(max_sum, window)

            l += 1
        
        return max_sum / float(k)




        # max_sum = -1 * float("inf")
        # for i in range(len(nums)-k+1):
        #     cur_sum = 0            
        #     for j in range(i, i+k):
        #         cur_sum += nums[j]

        #     max_sum = max(max_sum, cur_sum)

        
        # return float(max_sum) / float(k)













        # currSum = sum(nums[:k])
        # maxSum = currSum
        # l, r = 0, k
        # while r < len(nums):
        #     currSum += nums[r]
        #     currSum -= nums[l]
        #     l += 1
        #     r += 1

        #     if currSum > maxSum:
        #         maxSum = currSum

        # return maxSum / (k * 1.0)


        # l = 0
        # window = 0
        # for i in range(k):
        #     window += nums[i]
        # r = k
        # maxAverage = float('-inf')
        # maxAverage = max(maxAverage, float(window) / float(k))
        # while r < len(nums):
        #     window += nums[r]
        #     window -= nums[l]
        #     r += 1
        #     l += 1

        #     maxAverage = max(maxAverage, float(window) / float(k))

        
        # return maxAverage


        # maxVal = -1 * float('inf')
        # for i in range(len(nums)-k+1):
        #     temp = 0
        #     for j in range(i, i+k):
        #         temp += nums[j]
        #     maxVal = max(maxVal, temp)

        # return float(maxVal) / float(k)








        # l = 0
        # r = k
        # curr_max = sum(nums[:k])
        # maximum = curr_max
        # while r < len(nums):
        #     curr_max -= nums[l]
        #     curr_max += nums[r]
        #     l += 1
        #     r += 1
        #     if curr_max > maximum:
        #         maximum = curr_max
        # return (maximum/(k * 1.0))
