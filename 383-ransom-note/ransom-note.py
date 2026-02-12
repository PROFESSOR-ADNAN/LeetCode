class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
            count_magazine = Counter(magazine)
            count_ransomNote = Counter(ransomNote)

            for key, value in count_ransomNote.items():
                if key not in count_magazine or count_magazine[key] < value:
                    return False

            return True