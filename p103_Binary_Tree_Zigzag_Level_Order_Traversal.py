'''
- Leetcode problem: 103

- Difficulty: Medium

- Brief problem description:

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right
to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

- Solution Summary:

Use BFS with deque, but go through the queue twice. First time, we always go through left to right because we have to
make sure the order of nodes in the next level

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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        q = collections.deque()
        if root:
            q.append(root)

        reverse = False
        while q:
            n = len(q)
            currentLevel = []
            nextLevel = []

            for i in range(n):
                node = q.popleft()
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
                q.append(node)

            for i in range(n):
                if not reverse:
                    node = q.popleft()
                else:
                    node = q.pop()
                currentLevel.append(node.val)

            for j in range(len(nextLevel)):
                q.append(nextLevel[j])

            reverse = (not reverse)
            result.append(currentLevel)

        return result
