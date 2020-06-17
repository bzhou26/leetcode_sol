'''
- Leetcode problem: 250

- Difficulty: Medium

- Brief problem description:

Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4

- Solution Summary:

Bottom up solution

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
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.countTree(root)[0]

    def countTree(self, root):
        if root.left is None and root.right is None:
            return (1, True)

        if root.left is None:
            count, isUni = self.countTree(root.right)
            if root.val == root.right.val and isUni:
                return (count + 1, True)
            else:
                return (count, False)
        if root.right is None:
            count, isUni = self.countTree(root.left)
            if root.val == root.left.val and isUni:
                return (count + 1, True)
            else:
                return (count, False)
        leftCount, isUni_left = self.countTree(root.left)
        rightCount, isUni_right = self.countTree(root.right)
        if root.val == root.right.val and root.val == root.left.val and isUni_left and isUni_right:
            return (leftCount + rightCount + 1, True)

        return (leftCount + rightCount, False)
