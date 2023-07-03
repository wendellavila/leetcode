import unittest
"""
LeetCode problem
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

https://leetcode.com/problems/add-binary/
"""

def addBinary(a: str, b: str) -> str:
    """
    1- Reverse strings to make looping from end to start easier
    2- Find biggest and smallest strings and iterate from index 0 to length of biggest
    3- In each column, sum digit from biggest, digit from smallest (if available at that index), and carry over.
        If sum is 0 or 1, concatenate sum to start of result. Carry over for next column is zero.
        If sum is 2, concatenate 0 to start of result. Carry over for next column is one.
        If sum is 3, concatenate 1 to start of result. Carry over for next column is one.
    """
    smallest = a[::-1] if len(a) <= len(b) else b[::-1]
    biggest = b[::-1] if len(b) >= len(a) else a[::-1]

    carry_over = 0
    result = ""
    for i in range(0, len(biggest)):
        column_sum = int(smallest[i]) + int(biggest[i]) + carry_over if len(smallest) > i else int(biggest[i]) + carry_over
        if column_sum <= 1:
            result = str(column_sum) + result
            carry_over = 0
        elif column_sum == 2:
            result = "0" + result
            carry_over = 1
        else:
            result = "1" + result
            carry_over = 1
    if carry_over > 0:
        result = str(carry_over) + result
    
    return result

class TestSolution(unittest.TestCase):
    """Unit tests using unittest module"""
    def test_case_1(self):
        INPUT_1 = "11"
        INPUT_2 = "1"
        EXPECTED = "100"
        OUTPUT = addBinary(INPUT_1, INPUT_2)

        print(f'\nInput: "{INPUT_1}", "{INPUT_2}"')
        print(f'Expected: "{EXPECTED}"')
        print(f'Output: "{OUTPUT}"')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT_1 = "1010"
        INPUT_2 = "1011"
        EXPECTED = "10101"
        OUTPUT = addBinary(INPUT_1, INPUT_2)

        print(f'\nInput: "{INPUT_1}", "{INPUT_2}"')
        print(f'Expected: "{EXPECTED}"')
        print(f'Output: "{OUTPUT}"')
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    print("Testing solution\n")
    unittest.main(verbosity=2)