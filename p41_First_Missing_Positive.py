'''
- Leetcode problem: 41

- Difficulty: Hard

- Brief problem description:

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] <= 0:
                nums.pop(i)
            else:
                i += 1
        nums = [0] + nums

        for j in range(len(nums)):
            cur = nums[j]
            if cur < 0:
                cur *= -1
            if cur < len(nums) and nums[cur] > 0:
                nums[cur] *= -1

        for i in range(1, len(nums)):
            if nums[i] > 0:
                return i

        return len(nums)
