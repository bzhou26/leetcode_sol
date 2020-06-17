'''
- Leetcode problem: 314

- Difficulty: Medium

- Brief problem description:

Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''

import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        orderMap = collections.defaultdict(list)
        dq = collections.deque()
        dq.append((root, 0))

        while dq:
            n = len(dq)
            for i in range(n):
                node, order = dq.popleft()
                if node:
                    orderMap[order].append(node.val)
                    dq.append((node.left, order - 1))
                    dq.append((node.right, order + 1))
        orderedDict = collections.OrderedDict(sorted(orderMap.items()))
        result = []
        for k, v in orderedDict.items():
            result.append(v)

        return result
