'''
- Leetcode problem: 124

- Difficulty: Hard

- Brief problem description:

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the
parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

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
    def maxPathSum(self, root: TreeNode) -> int:
        maxSum = float('-inf')

        def calSum(node):
            nonlocal maxSum
            if node is None:
                return 0
            left = max(calSum(node.left), 0)
            right = max(calSum(node.right), 0)
            curSum = node.val + left + right
            maxSum = max(maxSum, curSum)
            return max(node.val + max(left, right), 0)

        calSum(root)

        return maxSum
