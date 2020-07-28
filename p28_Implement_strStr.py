'''
- Leetcode problem: 28

- Difficulty: Easy

- Brief problem description:

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr()
and Java's indexOf().

Constraints:

haystack and needle consist only of lowercase English characters.

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        cur = 0
        if len(needle) == 0:
            return 0
        found = False
        while i < len(haystack) - len(needle) + 1:
            for j in range(len(needle)):
                if haystack[i+j] == needle[j]:
                    if j == 0:
                        cur = i
                    if j == len(needle) - 1:
                        found = True
                else:
                    break
            if found:
                return i
            i += 1
        return -1
