'''
- Leetcode problem: 167

- Difficulty: Easy

- Brief problem description:

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

- Solution Summary:

Two index O(n) time and O(1) space

- Used Resources:

--- Bo Zhou
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1
        while low < high:
            twoSum = numbers[low] + numbers[high]
            if twoSum == target:
                return [low + 1, high + 1]
            elif twoSum > target:
                high -= 1
            else:
                low += 1
        return []
