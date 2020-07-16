'''
- Leetcode problem: 50

- Difficulty: Medium

- Brief problem description:

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1

        if n < 0:
            x = 1 / x
            n = -n

        return self.cal(x, n)

    def cal(self, x, n):
        if n == 0:
            return 1

        part = self.cal(x, n // 2)

        if (n % 2 == 0):
            return part * part
        else:
            return part * part * x
