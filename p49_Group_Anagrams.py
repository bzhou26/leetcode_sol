'''
- Leetcode problem: 49

- Difficulty: Medium

- Brief problem description:

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for w in strs:
            chars = list(w)
            chars.sort()
            d[tuple(chars)].append(w)
        result = []
        for k, v in d.items():
            result.append(v)

        return result