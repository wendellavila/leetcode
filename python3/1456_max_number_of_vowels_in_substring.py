import unittest
from typing import List
"""
LeetCode problem
1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of
vowel letters in any substring of s with length k.

https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
"""

def vowelCount(s:str) -> int:
    return sum(letter in ['a', 'e', 'i', 'o', 'u'] for letter in s)

def maxVowels(s: str, k: int) -> int:
    max_count = vowelCount(s[0:k])
    if max_count == k:
        return k

    for i in range(1, len(s)+1-k):
        curr_count = vowelCount(s[i:i+k])
        if curr_count == k:
            return k
        elif curr_count > max_count:
            max_count = curr_count
    return max_count

class TestSolution(unittest.TestCase):
    """Unit tests using unittest module"""
    def test_case_1(self):
        INPUT_1 = "abciiidef"
        INPUT_2 = 3
        EXPECTED = 3
        OUTPUT = maxVowels(INPUT_1, INPUT_2)

        print(f'\nInput: {INPUT_1}, {INPUT_2}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT_1 = "aeiou"
        INPUT_2 = 2
        EXPECTED = 2
        OUTPUT = maxVowels(INPUT_1, INPUT_2)

        print(f'\nInput: {INPUT_1}, {INPUT_2}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_3(self):
        INPUT_1 = "leetcode"
        INPUT_2 = 2
        EXPECTED = 2
        OUTPUT = maxVowels(INPUT_1, INPUT_2)

        print(f'\nInput: {INPUT_1}, {INPUT_2}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    print("Testing solution\n")
    unittest.main(verbosity=2)