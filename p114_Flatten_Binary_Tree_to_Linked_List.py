'''
- Leetcode problem: 114

- Difficulty: Medium

- Brief problem description:

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

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
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is not None:
            self.dfs(root)
        return

    def dfs(self, node):
        if node.left is None and node.right is None:
            return node
        while node.left or node.right:
            if node.left:
                pre_node = node.right
                node.right = node.left
                node.left = None
                end_node = self.dfs(node.right)

                end_node.right = pre_node
            if node.right:
                node = node.right
        return node
