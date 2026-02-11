class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count_of_chars = Counter(chars)
        ans = 0

        for word in words:
            count_of_word = Counter(word)
            for key, value in count_of_word.items():
                if key not in count_of_chars or count_of_word[key] > count_of_chars[key]:
                    break
            else:
                ans += len(word)

        return ans
