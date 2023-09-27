import unittest
"""
LeetCode problem
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using
the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""

def canConstruct(ransomNote: str, magazine: str) -> bool:
    """
    For every letter in magazine, an entry is added to a dictionary linking the letter to its repetition count in the string.
    e.g. 'a' = 1 if 'a' only appears once in magazine
    The same is done for ransomNote.

    For each letter in ransomNote:
    If ransomnote needs a bigger amount of that letter than magazine can provide,
    i.e. the repetition count of ransomnote is bigger than magazine for a given letter,
    the function returns false.

    Otherwise, function returns true.
    """
    ransom_dict = {}
    magazine_dict = {}
    
    for letter in magazine:
        if magazine_dict.get(letter) is None:
            magazine_dict[letter] = 1
        else:
            magazine_dict[letter] = magazine_dict.get(letter) + 1

    for letter in ransomNote:
        if magazine_dict.get(letter) is None:
            return False

        if ransom_dict.get(letter) is None:
            ransom_dict[letter] = 1
        else:
            ransom_dict[letter] = ransom_dict.get(letter) + 1

        if ransom_dict[letter] > magazine_dict.get(letter):
            return False
    return True

class TestSolution(unittest.TestCase):
    """Unit tests using unittest module"""
    def test_case_1(self):
        INPUT_1 = "a"
        INPUT_2 = "b"
        EXPECTED = False
        OUTPUT = canConstruct(INPUT_1, INPUT_2)
        
        print(f'\nInput: "{INPUT_1}" "{INPUT_2}"')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT_1 = "aa"
        INPUT_2 = "ab"
        EXPECTED = False
        OUTPUT = canConstruct(INPUT_1, INPUT_2)

        print(f'\nInput: "{INPUT_1}" "{INPUT_2}"')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_3(self):
        INPUT_1 = "aa"
        INPUT_2 = "aab"
        EXPECTED = True
        OUTPUT = canConstruct(INPUT_1, INPUT_2)

        print(f'\nInput: "{INPUT_1}" "{INPUT_2}"')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    print("Testing solution\n")
    unittest.main(verbosity=2)