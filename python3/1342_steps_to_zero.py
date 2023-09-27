import unittest
"""
LeetCode problem
1342. Number of Steps to Reduce a Number to Zero

Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
"""

def numberOfSteps(num: int) -> int:
    steps = 0
    while num != 0:
        num = num/2 if num % 2 == 0 else num - 1
        steps += 1
    
    return steps

class TestSolution(unittest.TestCase):
    """Unit tests using unittest module"""
    def test_case_1(self):
        INPUT = 14
        EXPECTED = 6
        OUTPUT = numberOfSteps(INPUT)

        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT = 8
        EXPECTED = 4
        OUTPUT = numberOfSteps(INPUT)

        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_3(self):
        INPUT = 123
        EXPECTED = 12
        OUTPUT = numberOfSteps(INPUT)

        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    print("Testing solution\n")
    unittest.main(verbosity=2)