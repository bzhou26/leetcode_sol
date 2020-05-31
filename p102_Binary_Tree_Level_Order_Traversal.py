'''
- Leetcode problem: 102

- Difficulty: Medium

- Brief problem description:

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

- Solution Summary:

BFS solution with deque

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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []

        q = collections.deque()
        if root:
            q.append(root)

        while q:
            n = len(q)
            currentLevel = []
            for i in range(n):
                node = q.popleft()
                currentLevel.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(currentLevel)

        return result
