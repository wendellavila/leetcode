import unittest
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: Optional[ListNode]) -> bool:
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
