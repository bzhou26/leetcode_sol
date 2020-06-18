'''
- Leetcode problem: 39

- Difficulty: Medium

- Brief problem description:

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique
combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.calSum(candidates, [], 0, target, 0, result)
        return result

    def calSum(self, candidates, combined, comSum, target, curIndex, result):
        if comSum == target:
            result.append(combined[:])
            return
        if comSum > target:
            return
        else:
            for i in range(curIndex, len(candidates)):
                combined.append(candidates[i])
                curSum = comSum + candidates[i]
                self.calSum(candidates, combined, curSum, target, i, result)
                combined.pop()
                if curSum >= target:
                    break
