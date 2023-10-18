import unittest
from typing import List
"""
LeetCode problem
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum
average alue and return this value.
Any answer with a calculation error less than 10-5 will be accepted.

https://leetcode.com/problems/roman-to-integer/
"""

def findMaxAverage(nums: List[int], k: int) -> float:
    maxAvg = sum(nums[0:k]) / k
    for i in range(1, len(nums)+1-k):
        currAvg = sum(nums[i:i+k]) / k
        if currAvg > maxAvg:
            maxAvg = currAvg
    return maxAvg

class TestSolution(unittest.TestCase):
    """Unit tests using unittest module"""
    def test_case_1(self):
        INPUT_1 = [1,12,-5,-6,50,3]
        INPUT_2 = 4
        EXPECTED = 12.75
        OUTPUT = findMaxAverage(INPUT_1, INPUT_2)

        print(f'\nInput: {INPUT_1}, {INPUT_2}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT_1 = [5]
        INPUT_2 = 1
        EXPECTED = 5.0
        OUTPUT = findMaxAverage(INPUT_1, INPUT_2)

        print(f'\nInput: {INPUT_1}, {INPUT_2}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_3(self):
        INPUT_1 = [0,1,1,3,3]
        INPUT_2 = 4
        EXPECTED = 2.0
        OUTPUT = findMaxAverage(INPUT_1, INPUT_2)

        print(f'\nInput: {INPUT_1}, {INPUT_2}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    print("Testing solution\n")
    unittest.main(verbosity=2)