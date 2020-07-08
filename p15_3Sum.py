'''
- Leetcode problem: 15

- Difficulty: Medium

- Brief problem description:

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets
in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

- Solution Summary:

Use dict to generate a 2 sum map, be careful for duplication result

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums) - 1):
            index = len(nums) - 1
            for j in range(i + 1, index):
                a = nums[i]
                b = nums[j]
                if a == 0 and b == 0 and (0,0,0) in result:
                    break
                c = 0 - a - b
                if c < b:
                    break
                while nums[index] > c and index > j:
                    index -= 1
                if nums[index] == c and index > j:
                    result.add((a, b, c))
        return list(result)
