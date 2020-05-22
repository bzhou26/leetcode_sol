'''
- Leetcode problem: 17

- Difficulty: Medium

- Brief problem description:

    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

- Solution Summary:

Typical backtrack solution
PS: remove last character in the for loop

- Used Resources:

--- Bo Zhou
'''


class Solution:
    keyMap = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def letterCombinations(self, digits):
        result = []
        if len(digits) > 0:
            self.combine('', digits, result)
        return result

    def combine(self, combined, digits, result):
        if len(digits) == 0:
            result.append(combined)
        else:
            for character in self.keyMap[int(digits[0])]:
                combined += character
                self.combine(combined, digits[1:], result)
                combined = combined[:-1]


if __name__ == "__main__":
    solution = Solution()
    testList = '23'
    print(solution.letterCombinations(testList))