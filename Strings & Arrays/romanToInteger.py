class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        roman_sum = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and s[i]+s[i+1] in lookup:
                roman_sum += lookup[s[i]+s[i+1]]
                i += 1
            else:
                roman_sum += lookup[s[i]]
            i += 1
        return roman_sum