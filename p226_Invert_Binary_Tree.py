'''
- Leetcode problem: 226

- Difficulty: Easy

- Brief problem description:

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard
 so f*** off.

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
    def invertTree(self, root: TreeNode) -> TreeNode:
        dq = deque()
        if root:
            dq.append(root)
        while dq:
            n = len(dq)
            for i in range(n):
                node = dq.pop()
                node.left, node.right = node.right, node.left
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return root
