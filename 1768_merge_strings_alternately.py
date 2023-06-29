import unittest
"""
LeetCode problem
1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

https://leetcode.com/problems/merge-strings-alternately/
"""

def mergeAlternately(word1: str, word2: str) -> str:
    """
    Get size of smallest string
    iterate from zero to min_size concatenating one character of both strings to the "merged" string
    If there's a biggest string, concatenate the remainder of that string to "merged"
    """
    min_length = len(word1) if len(word1) <= len(word2) else len(word2)
    merged = ""

    for i in range(0, min_length):
        merged += word1[i] + word2[i]
    
    if len(word1) > min_length:
        merged += word1[min_length:len(word1)]
    if len(word2) > min_length:
        merged += word2[min_length:len(word2)]
        
    return merged

def mergeAlternatelyRecursive(word1:str, word2:str) -> str:
    """Return the concatenation between the head of both strings and call function recursively for the tails.
    If the smaller tail is empty, return biggest tail
    If both tais are empty, return ""
    """
    smallest = word1 if len(word1) <= len(word2) else word2
    biggest = word2 if smallest == word1 else word1

    if len(smallest) > 0:
        return word1[0] + word2[0] + mergeAlternatelyRecursive(word1[1:len(word1)], word2[1:len(word2)])
    else:
        if len(biggest) > 0:
            return biggest
        else:
            return ""

class TestSolution(unittest.TestCase):
    """Unit tests using unittest module"""
    def test_case_1(self):
        INPUT_1 = "abc"
        INPUT_2 = "pqr"
        EXPECTED = "apbqcr"
        OUTPUT = mergeAlternately(INPUT_1, INPUT_2)

        print(f'\nInput: "{INPUT_1}", "{INPUT_2}"')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT_1 = "ab"
        INPUT_2 = "pqrs"
        EXPECTED = "apbqrs"
        OUTPUT = mergeAlternately(INPUT_1, INPUT_2)

        print(f'\nInput: "{INPUT_1}", "{INPUT_2}"')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_3(self):
        INPUT_1 = "abcd"
        INPUT_2 = "pq"
        EXPECTED = "apbqcd"
        OUTPUT = mergeAlternately(INPUT_1, INPUT_2)

        print(f'\nInput: "{INPUT_1}", "{INPUT_2}"')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_recursive_1(self):
        INPUT_1 = "abc"
        INPUT_2 = "pqr"
        EXPECTED = "apbqcr"
        OUTPUT = mergeAlternatelyRecursive(INPUT_1, INPUT_2)

        print(f'\nInput: "{INPUT_1}", "{INPUT_2}"')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_recursive_2(self):
        INPUT_1 = "ab"
        INPUT_2 = "pqrs"
        EXPECTED = "apbqrs"
        OUTPUT = mergeAlternatelyRecursive(INPUT_1, INPUT_2)

        print(f'\nInput: "{INPUT_1}", "{INPUT_2}"')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_recursive_3(self):
        INPUT_1 = "abcd"
        INPUT_2 = "pq"
        EXPECTED = "apbqcd"
        OUTPUT = mergeAlternatelyRecursive(INPUT_1, INPUT_2)

        print(f'\nInput: "{INPUT_1}", "{INPUT_2}"')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    print("Testing solution\n")
    unittest.main(verbosity=2)