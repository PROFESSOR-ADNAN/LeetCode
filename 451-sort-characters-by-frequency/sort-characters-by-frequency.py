class Solution:
    def frequencySort(self, s: str) -> str:
        # count = Counter(s)
        # temp = []
        # for key, value in count.items():
        #     temp.append([value, key])

        # temp.sort(reverse=True)
        # ans = ""
        # for value, key in temp:
        #     for i in range(value):
        #         ans += key

        # return ans

        count = Counter(s)
        bucket = defaultdict(list)

        for key, value in count.items():
            bucket[value].append(key)

        ans = []
        for i in range(len(s), 0, -1):
            for ch in bucket[i]:
                ans.append(ch * i)
        
        return "".join(ans)