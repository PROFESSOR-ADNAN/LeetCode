class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        def swap(i, j):
            heights[i], heights[j] = heights[j], heights[i]
            names[i], names[j] = names[j], names[i]

        n = len(heights)
        for i in range(n):
            swapped = False
            for j in range(n-i-1):
                if heights[j] < heights[j+1]:
                    swap(j, j+1)
                    swapped = True
            
            if not swapped:
                break
        
        return names
                    