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

class Solution(object):
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
            