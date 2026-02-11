class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            temp = []

            while num:
                last_digit = num % 10
                temp.append(last_digit)
                num //= 10

            for i in range(len(temp)-1, -1, -1):
                answer.append(temp[i])

        return answer
            
