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

        
        def flip(l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        n = len(arr)
        ans = []

        for i in range(n):
            mx = max(arr[:n-i])
            ind = arr.index(mx)

            flip(0, ind)
            flip(0, n-i-1)

            ans.append(ind+1)
            ans.append(n-i)

        return ans

        
