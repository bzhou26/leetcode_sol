'''
- Leetcode problem: 5

- Difficulty: Medium

- Brief problem description:

    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.

Example:

Input: "cbbd"

Output: "bb"

- Solution Summary:

1. There are 2N-1 centres, expend each centre to check the longest palindromic substring.

- Used Resources:

--- Bo Zhou

'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longestStr = ""
        for i in range(len(s)):
            palStr = self.expendStr(s, i, 1)
            if len(palStr) > len(longestStr):
                longestStr = palStr
            if i < len(s) - 1:
                palStr = self.expendStr(s, i, 2)
                if len(palStr) > len(longestStr):
                    longestStr = palStr
        return longestStr

    def expendStr(self, s, i, num):
        result = ""
        if num == 1:
            left = i - 1
            right = i + 1
            result = s[i]
        if num == 2:
            left = i
            right = i + 1
        while left >= 0 and right <= len(s) - 1:
            if s[left] == s[right]:
                result = s[left] + result + s[right]
            else:
                break
            left -= 1
            right += 1
        return result

if __name__ == "__main__":
    test = Solution()
    testStr1 = "cbbd"
    testStr2 = "babad"
    print(test.longestPalindrome(testStr1))
    print(test.longestPalindrome(testStr2))