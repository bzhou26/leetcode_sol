'''
- Leetcode problem: 1110

- Difficulty: Medium

- Brief problem description:

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.



Example 1:

           1
        /   \
       2     3
    /   \   /  \
   4    5  6   7


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]


Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.

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
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        result = []
        dq = deque()
        if root is None:
            return result

        dq.append((None, root, -1))
        to_delete_set = set(to_delete)
        if root.val not in to_delete_set:
            result.append(root)

        while dq:
            n = len(dq)
            for i in range(n):
                pre, node, direct = dq.popleft()
                needDel = node.val in to_delete_set
                if needDel and pre is not None:
                    if direct == 0:
                        pre.left = None
                    if direct == 1:
                        pre.right = None
                if node.left:
                    dq.append((node, node.left, 0))
                    if needDel and node.left.val not in to_delete_set:
                        result.append(node.left)
                if node.right:
                    dq.append((node, node.right, 1))
                    if needDel and node.right.val not in to_delete_set:
                        result.append(node.right)

        return result
