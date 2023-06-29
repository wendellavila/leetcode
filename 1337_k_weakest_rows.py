import unittest
from typing import List
"""
LeetCode problem
1337. The K Weakest Rows in a Matrix

You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
"""

def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    row_strength = {}

    for i in range(0, len(mat)):
        count = 0
        for j in range(0, len(mat[i])):
            if mat[i][j] == 1:
                count += 1
        row_strength[i] = count
        
    sorted_strength = sorted(row_strength, key=row_strength.get)
    return sorted_strength[0:k]

class TestSolution(unittest.TestCase):
    """Unit tests using unittest module"""
    def test_case_1(self):
        INPUT_MAT = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
        INPUT_K = 3
        EXPECTED = [2,0,3]
        OUTPUT = kWeakestRows(INPUT_MAT, INPUT_K)

        print(f'\nInput: {INPUT_MAT}, {INPUT_K}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT_MAT = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
        INPUT_K = 2
        EXPECTED = [0,2]
        OUTPUT = kWeakestRows(INPUT_MAT, INPUT_K)

        print(f'\nInput: {INPUT_MAT}, {INPUT_K}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    print("Testing solution\n")
    unittest.main(verbosity=2)