class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # divisor = []
        # div = 1
        # loop = 1
        # for num in nums:
        #     while div * 10 <= num:
        #         div *= 10
        #     divisor.append(div)

        # while True:
        #     for i in range(1, len(nums)):
        #         prev = nums[i-1]
        #         curr = nums[i]

        #         d1 = divisor[i-1]
        #         d2 = divisor[i]

        #         f1 = prev // d1
        #         f2 = prev // d2

        # divisorMpp = {}
        # div = 1
        # for num in nums:
        #     while div * 10 <= num:
        #         div *= 10
        #     divisorMpp[num] = div


        # for i in range(1, len(nums)):
        #     key = nums[i]
        #     j = i
        #     while j > 0:
        #         dk = divisorMpp[key]
        #         if dk:
        #             fk = key // dk

        #         num = nums[j-1]
        #         dj = divisorMpp[nums[j-1]]
        #         if dj:
        #             fj = num // dj

        #         print(fk, fj)
        #         if fk == fj:
        #             key %= dk
        #             num %= dj

        #             divisorMpp[nums[j]] //= 10
        #             divisorMpp[nums[j-1]] //= 10
                
        #             if not key or not num:
        #                 break
        #         elif fj > fk:
        #             nums[j], nums[j-1] = nums[j-1], nums[j]
        #             j -= 1
        #         else:
        #             break

        #         print(nums) 
        # return 0

        # totalNums = []
        # for num in nums:
        #     div = 1
        #     i = 0
        #     while div * 10 <= num:
        #         div *= 1
        #     while num:
        #         first_digit = num // div
        #         totalNums.append(first_digit)


        # divisorMpp = {}
        # div = 1
        # for num in nums:
        #     print(num)
        #     while div * 10 <= num:
        #         div *= 10
        #     print(div)
        #     divisorMpp[num] = div*10

        # for i in range(1, len(nums)):
        #     j = i
        #     while j > 0:
        #         ab = nums[j] * divisorMpp[nums[j-1]] + nums[j-1]
        #         ba = nums[j-1] * divisorMpp[nums[j]] + nums[j]
                
        #         print(divisorMpp[nums[j]])
        #         print(ab, ba)
        #         break

        #     break

        # return 0

        # for i in range(len(nums)):
        #     nums[i] = str(nums[i])

        # ans = []
        # path = []
        # visited = set()

        # def backtrack():
        #     if len(path) == len(nums):
        #         ans.append("".join(path))
        #         return

        #     for i in range(len(nums)):
        #         if i in visited:
        #             continue

        #         path.append(nums[i])
        #         visited.add(i)
        #         backtrack()
        #         path.pop()
        #         visited.remove(i)

        # backtrack()

        # mx = float("-inf")
        # for val in ans:
        #     mx = max(mx, int(val))

        # return str(mx)
        # for i in range(1, len(nums)):
        #     if nums[i][0] == nums[i-1][0]:
        #         curr = nums[i]
        #         j = i
        #         while j > 0 and len(curr[j]) > 1 and len(nums[j-1]) > 1 and curr[1] > nums[j-1][1]:
        #             nums[i] = nums[i-1]
        #             j -= 1

        #         nums[j] = curr

        # print(nums)

        # for i in range(len(nums)):
        #     nums[i] = str(nums[i])

        # def comparator(a, b):
        #     if a+b > b+a:
        #         return -1
        #     else:
        #         return 1

        # nums.sort(key=cmp_to_key(comparator))

        # return str(int("".join(nums)))




        for i in range(len(nums)):
            nums[i] = str(nums[i])

        def comparator(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(comparator))

        return str(int("".join(nums)))














