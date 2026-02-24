class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # if len(changed) % 2:
        #     return []

        # changed.sort()
        # print(changed)
        # left, right = 0, len(changed)//2
        # while left < right:
        #     print(changed[left], changed[right])
        #     if changed[left] * 2 != changed[right]:
        #         return []
        
        # return changed[:len(changed)//2]


        # mpp = {}
        # for num in changed:
        #     if (num*2) not in mpp and (num*2) in changed:
        #         mpp[num*2] = num
        #     print(num, mpp)

        # print()
        # print()

        # print("last", mpp)

        # return list(mpp.values())


        # if len(changed) % 2: return []

        # changed_sum = sum(changed)
        # original_sum = changed_sum // 3

        # n = len(changed)
        # half = n // 2
        
        # sum_ = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             sum_ = changed[i] + changed[j] + changed[k]
        #             if sum_ == original_sum:
        #                 return [changed[i], changed[j], changed[k]]
        #             sum_ -= changed[k]

        # return []


        # if len(changed) % 2: return []
        
        # changed_sum = sum(changed)
        # original_sum = changed_sum // 3

        # if changed_sum == original_sum: return changed[:len(changed)//2]

        # l, r = 0, len(changed)-1
        # changed.sort()
        
        # while r >= 0 and changed_sum - changed[r] > original_sum:
        #     changed_sum -= changed[r]
        #     r -= 1

        # print(l, r, changed_sum, original_sum, changed[l:r+1])
        # if r < 0:
        #     return []
        # elif changed_sum == original_sum:
        #     return changed[l:r+1]
        # else:
        #     removed = changed_sum - original_sum
        #     for i in range(l, r+1):
        #         if changed[i] == removed:
        #             return changed[:i] + changed[i+1:r+1]

        # return []

        # if len(changed) % 2:
        #     return []

        # changed_set = set(changed)
        # changed.sort()

        # n = len(changed)//2
        # ans = []

        # for i in range(n):
        #     val = changed[i]
        #     if val in changed_set:
        #         if (val * 2) not in changed_set:
        #             return []
        #         ans.append(val)
        #         changed_set.remove(val)
        #         changed_set.remove(val*2)

        # return ans
        

        if len(changed) % 2:
            return []

        changed_mpp = Counter(changed)
        changed.sort()

        n = len(changed)
        ans = []

        for i in range(n):
            val = changed[i]
            if val in changed_mpp:
                if (val * 2) not in changed_mpp:
                    return []
                ans.append(val)

                changed_mpp[val] -= 1
                if changed_mpp[val] == 0:
                    del changed_mpp[val]

                changed_mpp[val*2] -= 1
                if changed_mpp[val*2] == 0:
                    del changed_mpp[val*2]
                    
        return ans
        
