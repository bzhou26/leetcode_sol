'''
- Leetcode problem: 116

- Difficulty: Medium

- Brief problem description:

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The
binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be
set to NULL.

Initially, all next pointers are set to NULL.



Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


Example 1:



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to
its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers,
with '#' signifying the end of each level.

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        dq = deque()
        dq.append(root)

        while dq:
            n = len(dq)
            pre = dq.popleft()
            if pre.left:
                dq.append(pre.left)
            if pre.right:
                dq.append(pre.right)
            for i in range(1, n):
                cur = dq.popleft()
                pre.next = cur
                pre = cur
                if pre.left:
                    dq.append(pre.left)
                if pre.right:
                    dq.append(pre.right)
        return root
