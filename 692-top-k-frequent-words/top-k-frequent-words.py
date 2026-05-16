class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        freq = []
        for key, value in count.items():
            freq.append([-value, key])
        
        heapify(freq)
        ans = []
        for _ in range(k):
            _, word = heappop(freq)
            ans.append(word)

        return ans
