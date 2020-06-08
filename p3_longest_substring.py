'''
- Leetcode problem: 3

- Difficulty: Medium

- Brief problem description:

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        left = 0
        right = 0
        maxSet = set()
        while left < len(s) and right < len(s):
            if s[right] not in maxSet:
                maxSet.add(s[right])
                right += 1
                ans = max(ans, right - left)
            else:
                maxSet.remove(s[left])
                left += 1
        return ans
