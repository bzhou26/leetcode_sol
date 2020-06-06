'''
- Leetcode problem: 20

- Difficulty: Easy

- Brief problem description:

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def isValid(self, s: str) -> bool:
        pStack = []
        for c in s:
            if c == "{":
                pStack.append("}")
            elif c == "[":
                pStack.append("]")
            elif c == "(":
                pStack.append(")")
            elif len(pStack) == 0 or pStack.pop() != c:
                return False

        return len(pStack) == 0