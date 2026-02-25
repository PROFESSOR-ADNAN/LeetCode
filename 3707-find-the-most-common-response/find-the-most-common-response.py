class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        Row = len(responses)
        Col = len(responses[0])

        count = defaultdict(int)

        for r in range(Row):
            for element in set(responses[r]):
                count[element] += 1
        
        max_cnt = 0
        freq_response = []

        for key, value in count.items():
            print(key, value)
            if value > max_cnt:
                freq_response = []
                freq_response.append(key)
                max_cnt = value
            elif value == max_cnt:
                freq_response.append(key)
        

        freq_response.sort()
        return freq_response[0]

