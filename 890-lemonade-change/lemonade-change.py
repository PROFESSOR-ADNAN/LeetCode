class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveBirr = 0
        tenBirr = 0
        for bill in bills:
            if bill == 5:
                fiveBirr += 1
            elif bill == 10:
                tenBirr += 1
                fiveBirr -= 1
            else:
                if tenBirr > 0:
                    tenBirr -= 1
                    fiveBirr -= 1
                else:
                    fiveBirr -= 3

            if fiveBirr < 0:
                return False

        return True