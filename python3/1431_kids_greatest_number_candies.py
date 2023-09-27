import unittest
from typing import List
"""
LeetCode problem
1431. Kids With the Greatest Number of Candies

There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of
candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies,
they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
"""

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    biggest_no_extra = candies[0]
    for i in range(1, len(candies)):
        if candies[i] > biggest_no_extra:
            biggest_no_extra = candies[i]
    
    return list(map(lambda num: True if num + extraCandies >= biggest_no_extra else False, candies))

class TestSolution(unittest.TestCase):
    """Unit tests using unittest module"""
    def test_case_1(self):
        INPUT_LIST = [2,3,5,1,3]
        INPUT_EXTRA = 3
        EXPECTED = [True,True,True,False,True] 
        OUTPUT = kidsWithCandies(INPUT_LIST, INPUT_EXTRA)

        print(f'\nInput: {INPUT_LIST}, {INPUT_EXTRA}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT_LIST = [4,2,1,1,2]
        INPUT_EXTRA = 1
        EXPECTED = [True,False,False,False,False]
        OUTPUT = kidsWithCandies(INPUT_LIST, INPUT_EXTRA)

        print(f'\nInput: {INPUT_LIST}, {INPUT_EXTRA}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_3(self):
        INPUT_LIST = [12,1,12]
        INPUT_EXTRA = 10
        EXPECTED = [True,False,True]
        OUTPUT = kidsWithCandies(INPUT_LIST, INPUT_EXTRA)

        print(f'\nInput: {INPUT_LIST}, {INPUT_EXTRA}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    print("Testing solution\n")
    unittest.main(verbosity=2)