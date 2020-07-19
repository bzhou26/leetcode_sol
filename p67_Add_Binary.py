'''
- Leetcode problem: 67

- Difficulty: Easy

- Brief problem description:

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = ""
        while i >= 0 or j >= 0:
            l = 0
            r = 0
            if i >= 0:
                l = int(a[i])
            if j >= 0:
                r = int(b[j])
            t = l + r
            if t == 2:
                if carry == 1:
                    result = "1" + result
                else:
                    result = "0" + result
                    carry = 1
            elif t == 1:
                if carry == 1:
                    result = "0" + result
                else:
                    result = "1" + result
                    carry = 0
            else:
                result = str(carry) + result
                carry = 0
            i -= 1
            j -= 1

        if carry > 0:
            result = str(carry) + result

        return result
