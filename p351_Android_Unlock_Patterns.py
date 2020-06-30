'''
- Leetcode problem: 351

- Difficulty: Medium

- Brief problem description:

Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock
patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.



Rules for a valid pattern:

Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have
previously selected in the pattern. No jumps through non selected key is allowed.
The order of keys used matters.





Explanation:

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Invalid move: 4 - 1 - 3 - 6
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.



Example:

Input: m = 1, n = 1
Output: 9

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        invalidPattern = {
            1: [(2, 3), (4, 7), (5, 9)],
            2: [(5, 8)],
            3: [(2, 1), (5, 7), (6, 9)],
            4: [(5, 6)],
            6: [(5, 4)],
            7: [(4, 1), (5, 3), (8, 9)],
            8: [(5, 2)],
            9: [(5, 1), (6, 3), (8, 7)],
        }
        count = 0
        result = set()
        self.backTrack(set(), [], m, n, result, invalidPattern)
        return len(result)

    def backTrack(self, visited, combined, m, n, result, invalidPattern):
        if m <= len(combined) <= n:
            result.add(tuple(combined))

        if len(combined) == n:
            return

        for i in range(1, 10):
            if (i not in visited) and self.isValid(combined, i, invalidPattern):
                visited.add(i)
                self.backTrack(visited, combined + [i], m, n, result, invalidPattern)
                visited.remove(i)

    def isValid(self, combined, n, invalidPattern):
        if len(combined) == 0:
            return True

        last = combined[-1]
        pattern = invalidPattern.get(last, [])

        for block, target in pattern:
            if n == target and block not in combined:
                return False

        return True
