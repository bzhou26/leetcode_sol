'''
- Leetcode problem: 97

- Difficulty: Hard

- Brief problem description:

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

- Solution Summary:

Approach 3: Using 2D Dynamic Programming
Algorithm

https://leetcode.com/problems/interleaving-string/solution/

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) == 0:
            return s2 == s3
        elif len(s2) == 0:
            return s1 == s3
        elif len(s1) + len(s2) != len(s3):
            return False

        dp = [[False for i in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and (s2[j - 1] == s3[i + j - 1])
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and (s1[i - 1] == s3[i + j - 1])
                else:
                    curCheck = dp[i][j - 1] and (s2[j - 1] == s3[i + j - 1])
                    dp[i][j] = (dp[i - 1][j] and (s1[i - 1] == s3[i + j - 1])) or curCheck

        return dp[len(s1)][len(s2)]
