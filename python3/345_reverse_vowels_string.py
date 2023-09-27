import unittest
"""
LeetCode problem
345. Reverse Vowels of a String

Given a string s, find the order in which vowels appear in s and replace each vowel with the corresponding vowel in reverse order.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

https://leetcode.com/problems/reverse-vowels-of-a-string/
"""

def reverseVowels(s: str) -> str:
    """
    Navigate through the original string and add every vowel to a stack
    Make a copy of the original string
    For every vowel in the original string, pop a value from the stack and replace the vowel in the copy with it
    """
    VOWELS = ['a','e','i','o','u','A','E','I','O','U']
    vowel_stack = []
    for letter in s:
        if letter in VOWELS:
            vowel_stack.append(letter)

    reversed_s = s
    for i in range(0, len(s)):
        if s[i] in VOWELS:
            reversed_s = reversed_s[:i] + vowel_stack.pop() + reversed_s[i+1:]
    return reversed_s

class TestSolution(unittest.TestCase):
    """Unit tests using unittest module"""
    def test_case_1(self):
        INPUT = "hello"
        EXPECTED = "holle"
        OUTPUT = reverseVowels(INPUT)

        print(f'\nInput: "{INPUT}"')
        print(f'Expected: "{EXPECTED}"')
        print(f'Output: "{OUTPUT}"')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT = "leetcode"
        EXPECTED = "leotcede"
        OUTPUT = reverseVowels(INPUT)

        print(f'\nInput: "{INPUT}"')
        print(f'Expected: "{EXPECTED}"')
        print(f'Output: "{OUTPUT}"')
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    print("Testing solution\n")
    unittest.main(verbosity=2)