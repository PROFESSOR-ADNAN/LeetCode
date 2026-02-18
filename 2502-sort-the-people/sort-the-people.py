# class Solution:
#     def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
#         def swap(i, j):
#             heights[i], heights[j] = heights[j], heights[i]
#             names[i], names[j] = names[j], names[i]

#         n = len(heights)
#         for i in range(n):
#             swapped = False
#             for j in range(n-i-1):
#                 if heights[j] < heights[j+1]:
#                     swap(j, j+1)
#                     swapped = True
            
#             if not swapped:
#                 break
        
#         return names
                    

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        def swap(i, j):
            heights[i], heights[j] = heights[j], heights[i]
            names[i], names[j] = names[j], names[i]

        n = len(heights)
        for i in range(n):
            min_ind = i
            for j in range(i+1, n):
                if heights[j] > heights[min_ind]:
                    min_ind = j

            swap(i, min_ind)
            
        return names