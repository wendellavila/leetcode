import unittest
from typing import List
"""
LeetCode problem
412. Fizz Buzz

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""

def fizzBuzz(n: int) -> List[str]:

    answer = []
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            tmp = ""
            if i % 3 == 0:
                tmp += "Fizz"
            if i % 5 == 0:
                tmp += "Buzz"
            answer.append(tmp) 
        else:
            answer.append(str(i))
        
    return answer

class TestSolution(unittest.TestCase):
    """Unit tests using unittest module"""
    def test_case_1(self):
        INPUT = 3
        EXPECTED = ["1","2","Fizz"]
        OUTPUT = fizzBuzz(INPUT)
        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT = 5
        EXPECTED = ["1","2","Fizz","4","Buzz"]
        OUTPUT = fizzBuzz(INPUT)
        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_3(self):
        INPUT = 15
        EXPECTED = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
        OUTPUT = fizzBuzz(INPUT)
        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    print("Testing solution\n")
    unittest.main(verbosity=2)