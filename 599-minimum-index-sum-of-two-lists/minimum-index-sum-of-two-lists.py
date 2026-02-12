class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        min_index_sum = float("inf")

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if (i+j) < min_index_sum:
                        ans.clear()
                        ans.append(list1[i])
                        min_index_sum = (i+j)
                    elif (i+j) == min_index_sum:
                        ans.append(list1[i])

        return ans