class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        path = []
        def backtrack(i):
            if i == len(s):
                ans.append(" ".join(path[:]))
                return

            for j in range(i, len(s)):
                curr_split = s[i:j+1]

                if curr_split not in wordDict:
                    continue

                path.append(curr_split)
                backtrack(j+1)
                path.pop()

        backtrack(0)
        return ans
