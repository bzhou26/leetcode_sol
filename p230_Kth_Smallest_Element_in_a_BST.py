'''
- Leetcode problem: 230

- Difficulty: Medium

- Brief problem description:

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.



Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would
you optimize the kthSmallest routine?



Constraints:

The number of elements of the BST is between 1 to 10^4.
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

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
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        n_list = []
        dq = deque()
        dq.append(root)
        while dq:
            n = len(dq)
            for i in range(n):
                node = dq.popleft()
                n_list.append(node)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        n_list.sort(key=lambda x: x.val)
        return n_list[k-1].val
