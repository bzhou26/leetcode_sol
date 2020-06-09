'''
- Leetcode problem: 160

- Difficulty: Easy

- Brief problem description:

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.



Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the
head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the
intersected node in A; There are 3 nodes before the intersected node in B.


Example 2:


Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the
head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected
node in A; There are 1 node before the intersected node in B.

- Solution Summary:

Approach 3: Two Pointers
Maintain two pointers pApA and pBpB initialized at the head of A and B, respectively. Then let them both traverse
through the lists, one node at a time.
When pApA reaches the end of a list, then redirect it to the head of B (yes, B, that's right.); similarly when pBpB
reaches the end of a list, redirect it the head of A.
If at any point pApA meets pBpB, then pApA/pBpB is the intersection node.
To see why the above trick would work, consider the following two lists: A = {1,3,5,7,9,11} and B = {2,4,9,11}, which
are intersected at node '9'. Since B.length (=4) < A.length (=6), pBpB would reach the end of the merged list first,
because pBpB traverses exactly 2 nodes less than pApA does. By redirecting pBpB to head A, and pApA to head B, we now
ask pBpB to travel exactly 2 more nodes than pApA would. So in the second iteration, they are guaranteed to reach the
intersection node at the same time.
If two lists have intersection, then their last nodes must be the same one. So when pApA/pBpB reaches the end of a list,
record the last element of A/B respectively. If the two last elements are not the same one, then the two lists have no
intersections.

- Used Resources:

--- Bo Zhou
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        a_pointer = headA
        b_pointer = headB

        while a_pointer != b_pointer:
            if a_pointer:
                a_pointer = a_pointer.next
            else:
                a_pointer = headB
            if b_pointer:
                b_pointer = b_pointer.next
            else:
                b_pointer = headA

        return a_pointer