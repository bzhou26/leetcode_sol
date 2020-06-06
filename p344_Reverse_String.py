'''
- Leetcode problem: 344

- Difficulty: Easy

- Brief problem description:

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


# class Solution(object):
#     def reverseString(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         return s[::-1]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp
            i += 1
            j -= 1

        return s