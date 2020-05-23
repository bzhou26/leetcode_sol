'''
- Leetcode problem: 22

- Difficulty: Medium

- Brief problem description:

    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

- Solution Summary:

Use backtrack to solve the problem.

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def backTrack(self, combined, left, right, n, result):
        if len(combined) == 2 * n:
            result.append(combined)
            return
        if left < n:
            combined += '('
            self.backTrack(combined, left + 1, right, n, result)
            combined = combined[:-1]
        if left > right:
            combined += ')'
            self.backTrack(combined, left, right + 1, n, result)

    def generateParenthesis(self, n: int):
        result = []
        if (n > 0):
            self.backTrack('', 0, 0, n, result)
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3))