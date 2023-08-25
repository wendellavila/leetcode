import unittest
from typing import List
"""
LeetCode problem
443. String Compression

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

https://leetcode.com/problems/string-compression/
"""

def compress(chars: List[str]) -> int:

    compressed = ""
    prev = chars[0]
    count = 1

    for char in chars[1:]:
        if char == prev:
            count += 1
        else:
            compressed += prev
            if count > 1:
                compressed += str(count)
            prev = char
            count = 1
    
    compressed += prev
    if count > 1:
        compressed += str(count)

    for i in range(len(compressed)):
        chars[i] = compressed[i]

    del chars[len(compressed):]
    
    # Returning chars to facilitate unit tests
    # LeetCode solution should return length instead
    #return len(chars)
    return chars

class TestSolution(unittest.TestCase):
    """Unit tests using unittest module"""
    def test_case_1(self):
        INPUT = ["a","a","b","b","c","c","c"]
        EXPECTED = ["a","2","b","2","c","3"]
        OUTPUT = compress(INPUT)

        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT = ["a"]
        EXPECTED = ["a"]
        OUTPUT = compress(INPUT)

        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_3(self):
        INPUT = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        EXPECTED = ["a","b","1","2"]
        OUTPUT = compress(INPUT)

        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    print("Testing solution\n")
    unittest.main(verbosity=2)