'''
- Leetcode problem: 101

- Difficulty: Easy

- Brief problem description:

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


- Solution Summary:

Typical recursive solution

- Used Resources:

--- Bo Zhou
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.checkSymmetric(root.left, root.right)

    def checkSymmetric(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False

        if node1.val != node2.val:
            return False
        else:
            return self.checkSymmetric(node1.left, node2.right) and self.checkSymmetric(node1.right, node2.left)
