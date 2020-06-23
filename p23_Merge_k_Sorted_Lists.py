'''
- Leetcode problem: 23

- Difficulty: Hard

- Brief problem description:

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = []
        for l in lists:
            if l:
                heapq.heappush(pq, (l.val, id(l), l))
        newNode = ListNode()
        result = newNode
        while pq:
            minVal, i, minNode = heapq.heappop(pq)
            newNode.next = minNode
            nextNode = minNode.next
            newNode = minNode
            if nextNode:
                heapq.heappush(pq, (nextNode.val, id(nextNode), nextNode))

        return result.next
