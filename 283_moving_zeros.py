import unittest
from typing import List
"""
LeetCode Problem
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

https://leetcode.com/problems/move-zeroes/
"""
def moveZeroes(nums: List[int]):
    """
    Keeps a reference to the position currently
    being checked (left_index) and a reference to
    the position right before the last zero inclusion
    at the end (right_index)
    """
    left_index = 0
    right_index = len(nums)-1
    
    while left_index < right_index:
        if nums[left_index] == 0:
            current_val = nums[left_index]
            for i in range(left_index, right_index):
                nums[i] = nums[i+1]
            nums[right_index] = current_val
            right_index -= 1
        # second if can't be an else clause
        # it also needs to be run when first if
        # updates value in current position
        if nums[left_index] != 0:
            left_index += 1

    return nums

class TestSolution(unittest.TestCase):
    """Unit tests using unittest module"""
    def test_case_1(self):
        INPUT = [0,1,0,3,12]
        EXPECTED = [1,3,12,0,0]
        OUTPUT = moveZeroes(INPUT)

        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT = [0]
        EXPECTED = [0]
        OUTPUT = moveZeroes(INPUT)

        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_3(self):
        INPUT = [0,0,1]
        EXPECTED = [1,0,0]
        OUTPUT = moveZeroes(INPUT)

        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    print("Testing solution\n")
    unittest.main(verbosity=2)