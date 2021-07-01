class Solution:
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        prev_char = None
        val = 0
        for c in s:
            num = self.romans[c]
            if (c == 'V' or c == 'X') and prev_char == 'I':
                num -= self.romans['I'] * 2
            elif (c == 'L' or c == 'C') and prev_char == 'X':
                num -= self.romans['X'] * 2
            elif (c == 'D' or c == 'M') and prev_char == 'C':
                num -= self.romans['C'] * 2
            val += num
            prev_char = c
        return val


if __name__ == '__main__':
    s1 = 'III'
    s2 = 'IV'
    s3 = 'IX'
    s4 = 'LVIII'
    s5 = 'MCMXCIV'
    soln = Solution()
    assert soln.romanToInt(s1) == 3
    assert soln.romanToInt(s2) == 4
    assert soln.romanToInt(s3) == 9
    assert soln.romanToInt(s4) == 58
    assert soln.romanToInt(s5) == 1994
