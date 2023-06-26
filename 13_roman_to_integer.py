import unittest
"""
LeetCode problem
13. Roman to Integer

Given a roman numeral, convert it to an integer.

https://leetcode.com/problems/roman-to-integer/
"""

def romanToInt(s: str) -> int:
    """
    For each character in the string:
    If current character have a bigger corresponding value than the next character, add it to the total and repeat for the next.
    If current character have a smaller corresponding value than the next character, add the difference between the next character and the
    current to the total, skip the next character, and repeat for the character after the next.

    """
    toInt = 0
    values = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    skip_next = False

    for i in range(0, len(s)):
        if skip_next == False:
            if i+1 < len(s):
                if values[s[i]] >= values[s[i+1]]:
                    toInt += values[s[i]]
                    skip_next = False
                else:
                    toInt += values[s[i+1]] - values[s[i]]
                    skip_next = True
            else:
                toInt += values[s[i]]
                skip_next = False
        else:
            skip_next = False
    return toInt

class TestSolution(unittest.TestCase):
    """Unit tests using unittest module"""
    def test_case_1(self):
        INPUT = "III"
        EXPECTED = 3
        OUTPUT = romanToInt(INPUT)
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT = "LVIII"
        EXPECTED = 58
        OUTPUT = romanToInt(INPUT)
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_3(self):
        INPUT = "MCMXCIV"
        EXPECTED = 1994
        OUTPUT = romanToInt(INPUT)
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    unittest.main()