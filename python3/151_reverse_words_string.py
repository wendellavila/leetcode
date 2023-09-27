import unittest
"""
LeetCode problem
151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.

https://leetcode.com/problems/reverse-words-in-a-string/
"""

def reverseWords(s: str) -> str:
    """
    Split string on whitespace and add to a stack
    Pop each element of the stack, concatenating it to the output string adding whitespace when necessary
    """
    word_stack = s.split()
    reversed_s = ""

    while len(word_stack) > 0:
        reversed_s += word_stack.pop()
        if len(word_stack) > 0:
            reversed_s += " "
    return reversed_s

class TestSolution(unittest.TestCase):
    """Unit tests using unittest module"""
    def test_case_1(self):
        INPUT = "the sky is blue"
        EXPECTED = "blue is sky the"
        OUTPUT = reverseWords(INPUT)

        print(f'\nInput: "{INPUT}"')
        print(f'Expected: "{EXPECTED}"')
        print(f'Output: "{OUTPUT}"')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT = "  hello world  "
        EXPECTED = "world hello"
        OUTPUT = reverseWords(INPUT)

        print(f'\nInput: "{INPUT}"')
        print(f'Expected: "{EXPECTED}"')
        print(f'Output: "{OUTPUT}"')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_3(self):
        INPUT = "a good   example"
        EXPECTED = "example good a"
        OUTPUT = reverseWords(INPUT)

        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    print("Testing solution\n")
    unittest.main(verbosity=2)