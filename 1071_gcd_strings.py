import unittest
"""
LeetCode problem
1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

https://leetcode.com/problems/greatest-common-divisor-of-strings/
"""

def isDivisor(divisor:str, dividend:str) -> bool:
    """
    If the length of the dividend string is not a divisor of the length of the divisor string, return false
    Otherwise, slice divident in pieces of the same size as the divisor, checking if the slice is equal to the divisor
    If all slices are equal, return true, otherwise return false.
    """
    if len(dividend) % len(divisor) == 0:
        count = 0
        for j in range(0, len(dividend)//len(divisor)):
            tmp_slice = dividend[(j*len(divisor)):(j*len(divisor)+len(divisor))]
            if tmp_slice == divisor:
                count += 1
        if count == len(dividend)//len(divisor):
            return True
        else:
            return False
    else:
        return False

def gcdOfStrings(str1: str, str2: str) -> str:
    """
    Iterate through all substrings of the shortest strings that start with the first character of it,
    testing if it's a divisor of both original strings.
    """
    biggest = str1 if len(str1) >= len(str2) else str2
    shortest = str1 if biggest == str2 else str2

    for i in range(0, len(shortest)):
        divisor = shortest[0:len(shortest)-i]
        if isDivisor(divisor, shortest) and isDivisor(divisor, biggest):
            return divisor
        
    return ""

class TestSolution(unittest.TestCase):
    """Unit tests using unittest module"""
    def test_case_1(self):
        INPUT_1 = "ABCABC"
        INPUT_2 = "ABC"
        EXPECTED = "ABC"
        OUTPUT = gcdOfStrings(INPUT_1, INPUT_2)

        print(f'\nInput: "{INPUT_1}", "{INPUT_2}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT_1 = "ABABAB"
        INPUT_2 = "ABAB"
        EXPECTED = "AB"
        OUTPUT = gcdOfStrings(INPUT_1, INPUT_2)

        print(f'\nInput: "{INPUT_1}", "{INPUT_2}')
        print(f'Expected: "{EXPECTED}"')
        print(f'Output: "{OUTPUT}"')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_3(self):
        INPUT_1 = "LEET"
        INPUT_2 = "CODE"
        EXPECTED = ""
        OUTPUT = gcdOfStrings(INPUT_1, INPUT_2)

        print(f'\nInput: "{INPUT_1}", "{INPUT_2}')
        print(f'Expected: "{EXPECTED}"')
        print(f'Output: "{OUTPUT}"')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_4(self):
        INPUT_1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
        INPUT_2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
        EXPECTED = "TAUXX"
        OUTPUT = gcdOfStrings(INPUT_1, INPUT_2)

        print(f'\nInput: "{INPUT_1}", "{INPUT_2}')
        print(f'Expected: "{EXPECTED}"')
        print(f'Output: "{OUTPUT}"')
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    print("Testing solution\n")
    unittest.main(verbosity=2)