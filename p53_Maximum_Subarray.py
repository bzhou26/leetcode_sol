'''
- Leetcode problem: 53

- Difficulty: Easy

- Brief problem description:

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localMax = nums[0]
        globalMax = nums[0]
        for i in range(1, len(nums)):
            localMax = max(nums[i], localMax + nums[i])
            globalMax = max(globalMax, localMax)
        return globalMax
