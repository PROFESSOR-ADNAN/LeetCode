class Solution:
    def intToRoman(self, num: int) -> str:
        symbolToValue = {   1   : "I", 
                            5   : "V",
                            10  : "X",
                            50  : "L", 
                            100 : "C",
                            500 : "D", 
                            1000 : "M"
                        }
        
        roman = ""

        if num in symbolToValue:
            return symbolToValue[num]

        div = 1
        while div * 10 < num:
            div *= 10

        while num:
            first_digit = num // div
            
            if first_digit != 4 and first_digit != 9:
                if first_digit <= 3:
                    for i in range(first_digit):
                        roman += symbolToValue[div]
                else:
                    roman += symbolToValue[5 * div]
                    for i in range(first_digit - 5):
                        roman += symbolToValue[div]
            else:
                roman += symbolToValue[div]
                if first_digit == 4:
                    roman += symbolToValue[div*5]
                else:
                    roman += symbolToValue[div*10]
            
            num = num % div
            div = div // 10

        return roman

        