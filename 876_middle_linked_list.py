import unittest
from typing import Optional, List
"""
LeetCode problem
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

https://leetcode.com/problems/middle-of-the-linked-list/
"""
class ListNode:
    """Definition for singly-linked list"""
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
    def __str__(self, is_head=True):
        out = "[" + str(self.val) if is_head else str(self.val)
        if self.next:
            return out + "," + self.next.__str__(is_head=False)
        else:
            return out + "]"

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Navigate through list from start to end counting total of nodes
    Use total to find middle
    Navigate through list from start until middle and return middle
    """
    n = 0
    tmp_head = head

    while tmp_head is not None:
        n += 1
        tmp_head = tmp_head.next
    
    middle_index = n/2 + 0.5 if n % 2 == 1 else n/2 + 1
    
    n = 0
    while head is not None:
        n += 1
        if n == middle_index:
            return head
        head = head.next
    
    return None

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
        INPUT = self.build_linked_list([1,2,3,4,5])
        EXPECTED = 3
        OUTPUT = middleNode(INPUT).val

        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT = self.build_linked_list([1,2,3,4,5,6])
        EXPECTED = 4
        OUTPUT = middleNode(INPUT).val

        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    print("Testing solution\n")
    unittest.main(verbosity=2)