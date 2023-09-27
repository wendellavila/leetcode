import unittest
from typing import List
"""
LeetCode problem
1672. Richest Customer Wealth

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank.
Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth.

https://leetcode.com/problems/richest-customer-wealth/
"""

def maximumWealth(accounts: List[List[int]]) -> int:
    max_wealth = 0

    for customer in accounts:
        curr_wealth = 0
        for account in customer:
            curr_wealth += account
        if curr_wealth > max_wealth:
            max_wealth = curr_wealth

    return max_wealth

class TestSolution(unittest.TestCase):
    """Unit tests using unittest module"""
    def test_case_1(self):
        INPUT = [[1,2,3],[3,2,1]]
        EXPECTED = 6
        OUTPUT = maximumWealth(INPUT)

        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT = [[1,5],[7,3],[3,5]]
        EXPECTED = 10
        OUTPUT = maximumWealth(INPUT)

        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_3(self):
        INPUT = [[2,8,7],[7,1,3],[1,9,5]]
        EXPECTED = 17
        OUTPUT = maximumWealth(INPUT)

        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    print("Testing solution\n")
    unittest.main(verbosity=2)