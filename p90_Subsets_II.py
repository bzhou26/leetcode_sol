'''
- Leetcode problem: 90

- Difficulty: Medium

- Brief problem description:

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums) + 1):
            self.combineSet(nums, 0, [], result, i)
        return result

    def combineSet(self, nums, lastIndex, combined, result, k):
        if len(combined) == k:
            result.add(tuple(sorted(combined[:])))
            return
        for i in range(lastIndex, len(nums)):
            combined.append(nums[i])
            self.combineSet(nums, i + 1, combined, result, k)
            combined.pop()
