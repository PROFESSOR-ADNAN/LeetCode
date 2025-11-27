class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        for i in range(len(names)-1):
            min_ind = i
            for j in range(i+1, len(names)):
                if heights[j] > heights[min_ind]:
                    min_ind = j
            if min_ind != i:
                heights[i], heights[min_ind] = heights[min_ind], heights[i]
                names[i], names[min_ind] = names[min_ind], names[i]
        return names


        # combine = list(zip(names, heights))
        # combine = sorted(combine,key = lambda x:x[1], reverse=True)
        # name = [name for name, height in combine]
        # return name

        # for i in range(len(names)):
        #     for j in range(len(names)-i-1):
        #         if heights[j] < heights[j+1]:
        #             heights[j], heights[j+1] = heights[j+1], heights[j]
        #             names[j], names[j+1] = names[j+1], names[j]
        # return names

        
        
        
        # bubble sort
        # for i in range(len(names)):
        #     for j in range(len(names)-1-i):
        #         if heights[j] < heights[j+1]:
        #             heights[j], heights[j+1] = heights[j+1], heights[j]
        #             names[j], names[j+1] = names[j+1], names[j]

        # return names

        # selection sort
        # for i in range(len(names)):
        #     maxInd = i
        #     for j in range(i+1, len(names)):
        #         if heights[j] > heights[maxInd]:
        #             maxInd = j
        #     heights[i], heights[maxInd] = heights[maxInd], heights[i]
        #     names[i], names[maxInd] = names[maxInd], names[i]

        # return names


        # insertion sort
        # for i in range(1, len(names)):
        #     position = i
        #     val = heights[position]
        #     name_val = names[position]
        #     while position > 0 and val > heights[position-1]:
        #         heights[position] = heights[position-1]
        #         names[position] = names[position-1]
        #         position -= 1
        #     heights[position] = val
        #     names[position] = name_val
        
        # return names


        # count sort
        # count = [0] * (max(heights) + 1)
        # for height in heights:
        #     count[height] += 1
        
        # for i in range(1, len(count)):
        #     count[i] += count[i-1]

        # output_names = [0] * (len(names))

        # # for i in range(len(names)):
        # #     output_names[count[heights[i]]-1] = names[i]
        # i = len(names)-1
        # while i >= 0:
        #     output_names[count[heights[i]] - 1] = names[i]
        #     count[heights[i]] -= 1
        #     i -= 1
        
        # return output_names[::-1]


        # merge sort
        # def merge_sort(arr, names):
        #     if len(arr) <= 1:
        #         return [arr, names]
        #     mid = len(arr)//2
        #     left_arr, left = merge_sort(arr[:mid], names[:mid])
        #     right_arr, right = merge_sort(arr[mid:], names[mid:])

        #     i, j = 0, 0
        #     output = []
        #     new_names = []

        #     while i < len(left_arr) and j < len(right_arr):
        #         if left_arr[i] > right_arr[j]:
        #             output.append(left_arr[i])
        #             new_names.append(left[i])
        #             i += 1
        #         else:
        #             output.append(right_arr[j])
        #             new_names.append(right[j])
        #             j += 1

        #     while i < len(left_arr):
        #         output.append(left_arr[i])
        #         new_names.append(left[i])
        #         i += 1

            
        #     while j < len(right_arr):
        #         output.append(right_arr[j])
        #         new_names.append(right[j])
        #         j += 1

        #     return [output, new_names]

        # temp, res = merge_sort(heights, names)
        # return res

        # quick sort 
        def partition (arr, l, r):
            pivot = arr[r]
            i = l-1

            for j in range(l, r):
                if arr[j] >= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    names[i], names[j] = names[j], names[i]
            
            arr[i+1], arr[r] = arr[r], arr[i+1]
            names[i+1], names[r] = names[r], names[i+1]
            return i+1

        def quick_sort(arr, l, r):
            if l < r:
                p = partition(arr, l, r)

                quick_sort(arr, l, p-1)
                quick_sort(arr, p+1, r)
        
        quick_sort(heights, 0, len(heights)-1)
        return names            