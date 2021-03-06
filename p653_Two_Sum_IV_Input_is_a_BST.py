'''
- Leetcode problem: 653

- Difficulty: Easy

- Brief problem description:

    Given a Binary Search Tree and a target number,
    return true if there exist two elements in the BST such
    that their sum is equal to the given target.

Example 1:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True

Example 2:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

- Solution Summary:
1. Search the tree recursively, maintain a set of targets.

- Used Resources:

--- Bo Zhou

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        targets = set()
        return self.findTarget2(root, k, targets)

    def findTarget2(self, root, k, targets):
        if root == None:
            return False
        elif root.val in targets:
            return True
        else:
            targets.add(k - root.val)
            return self.findTarget2(root.left, k, targets) or self.findTarget2(root.right, k, targets)
