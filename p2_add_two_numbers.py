'''
2. Add Two Numbers
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current1 = l1
        current2 = l2
        currentResult = ListNode(None)
        result = currentResult
        carry = 0
        while (current1 != None) or (current2 != None) or (carry != 0):
            if current1 == None:
                num1 = 0
            else:
                num1 = current1.val
            if current2 == None:
                num2 = 0
            else:
                num2 = current2.val
            currentSum = num1 + num2 + carry
            carry = currentSum // 10
            currentResult.next = ListNode(currentSum % 10)
            currentResult = currentResult.next
            if current1 != None:
                current1 = current1.next
            if current2 != None:
                current2 = current2.next
        return result.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        result = ListNode(0)
        twoSum = result
        while l1 or l2 or carry:
            twoSum.next = ListNode(0)
            twoSum = twoSum.next
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            twoSum.val = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10


        return result.next
