'''
- Leetcode problem: 25

- Difficulty: Hard

- Brief problem description:

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.


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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next == None:
            return head

        pre_tail = None
        result_head = None

        while self.checkLengthValid(head, k):
            new_head, new_tail = self.reverseByN(head, k)
            if result_head == None:
                result_head = new_head
            if pre_tail != None:
                pre_tail.next = new_head
            pre_tail = new_tail
            head = new_tail.next

        return result_head

    # return tuple (head_node, tail_node)
    def reverseByN(self, head, n):
        pre = head
        cur = head.next
        i = 0
        while i < n - 1:
            pre.next = cur.next
            cur.next = head
            cur, head = pre.next, cur
            i += 1

        return head, pre

    def checkLengthValid(self, head, n):
        for i in range(n):
            if head == None:
                return False
            head = head.next
        return True
