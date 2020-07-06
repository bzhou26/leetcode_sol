'''
- Leetcode problem: 159

- Difficulty: Medium

- Brief problem description:

Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = 0
        r = 0

        seen = {}
        goLeft = False
        longest = 0
        while r < len(s):
            cur = s[l:r+1]
            if goLeft:
                if seen.get(s[l]) > 1:
                    seen[s[l]] = seen.get(s[l]) - 1
                elif seen.get(s[l]):
                    del seen[s[l]]
                if len(seen) < 2:
                    goLeft = False
                l += 1
            else:
                if seen.get(s[r]) or len(seen) < 2:
                    seen[s[r]] = seen.get(s[r], 0) + 1
                    longest = max(longest, r - l + 1)
                else:
                    goLeft = True
                if not goLeft:
                    r += 1

        return longest


if __name__ == "__main__":
    solution = Solution()
    testList = "eceba"
    print(solution.lengthOfLongestSubstringTwoDistinct(testList))
