import unittest
from typing import List
"""
LeetCode problem
605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

https://leetcode.com/problems/can-place-flowers/
"""

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    count = 0
    skip_next = False
    for i in range(0, len(flowerbed)):
        if skip_next == True:
            skip_next = False
        else:
            if canPositionBePlanted(flowerbed, i):
                count += 1
                skip_next = True
            
    return count >= n

def canPositionBePlanted(flowerbed: List[int], n: int) -> bool:
    if n < len(flowerbed):
        if flowerbed[n] == 0:
            if n-1 >= 0:
                is_left_free = True if flowerbed[n-1] == 0 else False
            else:
                is_left_free = True
            
            if n+1 < len(flowerbed):
                is_right_free = True if flowerbed[n+1] == 0 else False
            else:
                is_right_free = True
            return is_left_free and is_right_free
    return False


class TestSolution(unittest.TestCase):
    """Unit tests using unittest module"""
    def test_case_1(self):
        INPUT_ARR = [1,0,0,0,1]
        INPUT_N = 1
        EXPECTED = True
        OUTPUT = canPlaceFlowers(INPUT_ARR, INPUT_N)

        print(f'\nInput: {INPUT_ARR}, {INPUT_N}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT_ARR = [1,0,0,0,1]
        INPUT_N = 2
        EXPECTED = False
        OUTPUT = canPlaceFlowers(INPUT_ARR, INPUT_N)

        print(f'\nInput: {INPUT_ARR}, {INPUT_N}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    print("Testing solution\n")
    unittest.main(verbosity=2)