'''
- Leetcode problem: 543

- Difficulty: Easy

- Brief problem description:

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the
length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

- Solution Summary:

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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        result = [0]
        self.dfs(root, result)

        return result[0] - 1

    def dfs(self, node, result):
        if node is None:
            return 0
        l = self.dfs(node.left, result)
        r = self.dfs(node.right, result)
        result[0] = max(result[0], l + r + 1)
        return max(l, r) + 1
