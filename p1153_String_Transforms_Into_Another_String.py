'''
- Leetcode problem: 1304

- Difficulty: Hard

- Brief problem description:

Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero
or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.



Example 1:

Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
Example 2:

Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.


Note:

1 <= str1.length == str2.length <= 10^4
Both str1 and str2 contain only lowercase English letters.

- Solution Summary:

str2 need to contain less than 26 characters, otherwise it's impossible to translate.
See: https://leetcode.com/problems/string-transforms-into-another-string/discuss/681472/Explaining-why-Str2-needs-less-than-26-unique-characters

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        if len(str1) != len(str2):
            return False
        d = {}
        for i, j in zip(str1, str2):
            if d.setdefault(i, j) != j:
                return False
        return len(set(str2)) < 26
