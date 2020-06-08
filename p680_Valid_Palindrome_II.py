'''
- Leetcode problem: 680

- Difficulty: Easy

- Brief problem description:

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.checkPalindrome(s[i:j]) or self.checkPalindrome(s[i + 1: j + 1])
            i += 1
            j -= 1

        return True

    def checkPalindrome(self, s: str):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True