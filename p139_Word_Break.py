'''
- Leetcode problem: 139

- Difficulty: Medium

- Brief problem description:

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be
segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def wordBreak(self, s, wordDict):
        wordDictSet = set(wordDict)
        dp = [False for i in range(len(s) + 1)]
        for i in range(len(s) + 1):
            w = s[:i]
            if w in wordDictSet:
                dp[i] = True
            else:
                for j in range(i, -1, -1):
                    if dp[j] and s[j:i] in wordDictSet:
                        dp[i] = True
                        break

        return dp[len(s)]


if __name__ == "__main__":
    solution = Solution()
    testString = "leetcode"
    wordDict = ["leet", "code"]
    print(solution.wordBreak(testString, wordDict))