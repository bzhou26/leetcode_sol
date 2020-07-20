'''
- Leetcode problem: 203

- Difficulty: Easy

- Brief problem description:

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        node = head
        pre = None
        while node:
            if node.val == val:
                if pre is None:
                    head = head.next
                else:
                    pre.next = node.next
            else:
                pre = node
            node = node.next

        return head
