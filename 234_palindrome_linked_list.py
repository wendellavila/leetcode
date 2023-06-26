import unittest
from typing import Optional
"""
LeetCode problem
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

https://leetcode.com/problems/palindrome-linked-list/
"""
class ListNode:
    """Definition for singly-linked list"""
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: Optional[ListNode]) -> bool:
    """
    For each value in the input list, concatenate it to the start of a string and to the end of another string.
    If the two strings are equal at the end, input is palindrome.
    """
    values = ""
    values_inverse = ""

    while head is not None:
        values = values + str(head.val)
        values_inverse = str(head.val) + values_inverse
        head = head.next
    
    if values == values_inverse:
        return True
    else:
        return False

class TestSolution(unittest.TestCase):
    """Unit tests using unittest module"""
    def build_linked_list(self, values) -> ListNode:
        if len(values) > 0:
            head = ListNode(val=values[0])
            node = head
            for i in range(1, len(values)):
                next_node = ListNode(val=values[i])
                node.next = next_node
                node = next_node
            return head
        else:
            return None
    def test_case_1(self):
        INPUT = self.build_linked_list([1,2,2,1])
        EXPECTED = True
        OUTPUT = isPalindrome(INPUT)
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT = self.build_linked_list([1,2])
        EXPECTED = False
        OUTPUT = isPalindrome(INPUT)
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_3(self):
        INPUT = self.build_linked_list([1,2,2,3,2,2,1])
        EXPECTED = True
        OUTPUT = isPalindrome(INPUT)
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_4(self):
        INPUT = self.build_linked_list([1,2,2,3,2,2,3])
        EXPECTED = False
        OUTPUT = isPalindrome(INPUT)
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    unittest.main()
