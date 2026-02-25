class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        temp = []
        for key, value in count.items():
            temp.append([value, key])

        temp.sort(reverse=True)
        ans = ""
        for value, key in temp:
            for i in range(value):
                ans += key

        return ans
