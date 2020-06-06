'''
- Leetcode problem: 151

- Difficulty: Medium

- Brief problem description:

Given an input string, reverse the string word by word.



Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.


Follow up:

For C programmers, try to solve it in-place in O(1) extra space.

- Solution Summary:

[4, 7, 10, 13] k = 3

missing number = nums[i] - nums[0] - i

1. Binary Search to find the missing number.

7: 2 missing number before it
10: 4 missing number before it
So result is 7 + (k - missing number at 7)
Edge case: if k is larger enough that it's not contained in the list, we can return it directly.

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split()
        newS = " ".join(sList[::-1])
        return newS