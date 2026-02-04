class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""

        min_len = float("inf")
        for word in strs:
            if len(word) < min_len:
                min_len = len(word)
        
        for ind in range(min_len):
            curr_letter = set()
            for word in strs:
                curr_letter.add(word[ind])
            
            if len(curr_letter) == 1:
                answer += curr_letter.pop()
            else:
                break

        return answer