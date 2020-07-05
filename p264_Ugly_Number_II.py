'''
- Leetcode problem: 264

- Difficulty: Medium

- Brief problem description:

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        hp = []
        heapq.heappush(hp, 1)

        count = 0
        result = []
        seen = set()
        while count < n:
            cur = heapq.heappop(hp)
            result.append(cur)
            count += 1

            for i in [2, 3, 5]:
                if i * cur not in seen:
                    heapq.heappush(hp, i * cur)
                    seen.add(i * cur)

        return result[-1]
