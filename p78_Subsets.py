'''
- Leetcode problem: 78

- Difficulty: Medium

- Brief problem description:

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums) + 1):
            self.combineSet(nums, 0, [], result, i)
        return result

    def combineSet(self, nums, lastIndex, combined, result, k):
        if len(combined) == k:
            result.append(combined[:])
            return
        for i in range(lastIndex, len(nums)):
            combined.append(nums[i])
            self.combineSet(nums, i + 1, combined, result, k)
            combined.pop()
