'''
- Leetcode problem: 136

- Difficulty: Easy

- Brief problem description:

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         result = {}
#         for num in nums:
#             result[num] = result.get(num, 0) + 1
#         for key, val in result.items():
#             if val == 1:
#                 return key

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
