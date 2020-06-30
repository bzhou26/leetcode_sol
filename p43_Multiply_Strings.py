'''
- Leetcode problem: 43

- Difficulty: Medium

- Brief problem description:

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also
represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        for i in range(len(num1) - 1, -1, -1):
            n1 += (10 ** (len(num1) - 1 - i)) * int(num1[i])
        n2 = 0
        for i in range(len(num2) - 1, -1, -1):
            n2 += (10 ** (len(num2) - 1 - i)) * int(num2[i])

        return str(n1 * n2)
