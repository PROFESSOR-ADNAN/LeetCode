class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToLetterMap = {
                            "2": "abc",
                            "3": "def",
                            "4": "ghi",
                            "5": "jkl",
                            "6": "mno",
                            "7": "pqrs",
                            "8": "tuv",
                            "9": "wxyz"
                            }
        ans = []
        path = []
        def backtrack(i):
            if len(path) == len(digits):
                ans.append("".join(path))
                return

            if i >= len(digits):
                return

            curr = digits[i]
            letters = digitToLetterMap[curr]
            for j in range(len(letters)):
                currLetter = letters[j]
                path.append(currLetter)
                backtrack(i+1)
                path.pop()

        backtrack(0)
        return ans
            

