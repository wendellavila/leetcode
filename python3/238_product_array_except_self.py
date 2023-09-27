import unittest

"""
LeetCode problem
238. Product of Array Except Self

Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums
except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit
in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without
using the division operation.

https://leetcode.com/problems/product-of-array-except-self/
"""

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    # initialize list with ones so they can be multiplied without influencing the product
    left_prod = [1] * n
    right_prod = [1] * n

    # calculate only the product of positions to the left of current index
    # doing it in a loop reuses results from other positions
    # ex: left_prod[1] is nums[0]
    # left_prod[2] will be the result of left_prod[1] * nums[1]
    for i in range(1, n):
        left_prod[i] = left_prod[i-1] * nums[i-1]
    # same applies for right product
    for i in range(n-2, -1, -1):
        right_prod[i] = right_prod[i+1] * nums[i+1]
    return [left_prod[i] * right_prod[i] for i in range(n)]

class TestSolution(unittest.TestCase):
    """Unit tests using unittest module"""
    def test_case_1(self):
        INPUT = [1,2,3,4]
        EXPECTED = [24,12,8,6]
        OUTPUT = productExceptSelf(INPUT)

        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT = [-1,1,0,-3,3]
        EXPECTED = [0,0,9,0,0]
        OUTPUT = productExceptSelf(INPUT)

        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    print("Testing solution\n")
    unittest.main(verbosity=2)