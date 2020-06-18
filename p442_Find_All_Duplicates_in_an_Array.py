'''
- Leetcode problem: 442

- Difficulty: Medium

- Brief problem description:

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

- Solution Summary:

In-place solution, time: O(n), Memory: O(1)

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                result.append(abs(nums[i]))
            else:
                nums[abs(nums[i]) - 1] *= -1

        return result
