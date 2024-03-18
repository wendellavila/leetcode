import unittest
"""
LeetCode problem
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def maxDepth(node: TreeNode | None, current_depth: int = 1) -> int:
    if node is None:
        return 0
    else:
        if node.left is None and node.right is None:
            return current_depth
        elif node.left is None and node.right is not None:
            return maxDepth(node.right, current_depth+1)
        elif node.left is not None and node.right is None:
            return maxDepth(node.left, current_depth+1)
        else:
            return max(maxDepth(node.left, current_depth+1), maxDepth(node.right, current_depth+1))
    
def makeTree(lst: list[int | None] | None) -> TreeNode:
    if not lst:
        return None
    values = iter(lst)
    root = TreeNode(next(values))
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            children = [
                None if value is None else TreeNode(value)
                for value in (next(values, None), next(values, None))
            ]
            queue.extend(children)
            node.left, node.right = children
    return root

class TestSolution(unittest.TestCase):
    """Unit tests using unittest module"""
    def test_case_1(self):
        INPUT = makeTree([3,9,20,None,None,15,7])
        EXPECTED = 3
        OUTPUT = maxDepth(INPUT)

        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_2(self):
        INPUT = makeTree([1,None,2])
        EXPECTED = 2
        OUTPUT = maxDepth(INPUT)

        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)
    def test_case_3(self):
        INPUT = makeTree([])
        EXPECTED = 0
        OUTPUT = maxDepth(INPUT)

        print(f'\nInput: {INPUT}')
        print(f'Expected: {EXPECTED}')
        print(f'Output: {OUTPUT}')
        self.assertEqual(OUTPUT, EXPECTED)

if __name__ == '__main__':
    print("Testing solution\n")
    unittest.main(verbosity=2)