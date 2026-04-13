class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # n = len(arr)
        # ans = []

        # for i in range(n):
        #     mx = max(arr)
        #     ind = arr.index(mx)

        #     ans.append(ind+1)
        #     ans.append(n)

        #     arr[ind] = 0

        # return ans

        
        # def flip(l, r):
        #     while l < r:
        #         arr[l], arr[r] = arr[r], arr[l]
        #         l += 1
        #         r -= 1

        # n = len(arr)
        # ans = []

        # for i in range(n):
        #     mx = max(arr[:n-i])
        #     ind = arr.index(mx)

        #     flip(0, ind)
        #     flip(0, n-i-1)

        #     ans.append(ind+1)
        #     ans.append(n-i)

        # return ans

        def flip(end):
            start = 0
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        N = len(arr)
        ans = []

        for i in range(N-1, -1, -1):
            mx = i
            for j in range(i-1, -1, -1):
                if arr[j] > arr[mx]: mx = j

            if mx != i:
                flip(mx)
                flip(i)
                ans.append(mx+1)
                ans.append(i+1)

        return ans

        
