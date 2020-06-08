'''
- Leetcode problem: 46

- Difficulty: Medium

- Brief problem description:

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

- Solution Summary:

Recursive solution

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = set()
        self.permuteCal(nums, visited, [], result)

        return result

    def permuteCal(self, nums, visited, combined, result):
        if len(combined) == len(nums):
            result.append(combined[:])
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


if __name__ == "__main__":
    solution = Solution()
    testList = [1, 2, 3]
    print(solution.permute(testList))