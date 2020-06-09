'''
- Leetcode problem: 47

- Difficulty: Medium

- Brief problem description:

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

- Solution Summary:

Recursive solution

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()
        visited = set()

        self.permuteCal(nums, visited, [], result)

        return list(result)

    def permuteCal(self, nums, visited, combined, result):
        if len(combined) == len(nums):
            result.add(tuple(combined[:]))
            return
        i = 0
        while i < len(nums):
            if i not in visited:
                combined.append(nums[i])
                visited.add(i)
                self.permuteCal(nums, visited, combined, result)
                visited.remove(i)
                combined.pop()
            i += 1
