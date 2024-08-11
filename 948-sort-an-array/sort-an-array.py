class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge(Arr, L, Mid, R):
            left, right = Arr[L:Mid+1], Arr[Mid+1:R+1]
            i, j, k = 0, 0, L
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    Arr[k] = left[i]
                    i += 1
                else:
                    Arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                Arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                Arr[k] = right[j]
                j += 1
                k += 1
            

        def mergeSort(arr, l, r):
            if l == r:
                return arr
            mid = (l+r) // 2
            mergeSort(arr, l, mid)
            mergeSort(arr, mid+1, r)
            merge(arr, l, mid, r)
            return arr

        return mergeSort(nums, 0, len(nums)-1)
            

        

        

        