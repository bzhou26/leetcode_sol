'''
- Leetcode problem: 503

- Difficulty: Medium

- Brief problem description:

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater
Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next
in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1
for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        greaterMap = {}
        for i in range(len(nums)):
            if stack:
                while stack and nums[i] > stack[-1][0]:
                    num, index = stack.pop(-1)
                    greaterMap[index] = nums[i]
            stack.append((nums[i], i))

        while stack:
            num, index = stack.pop(0)
            greater = float('-inf')
            for i in range(index):
                if nums[i] > nums[index]:
                    greater = nums[i]
                    break
            if greater == float('-inf'):
                greater = -1
            greaterMap[index] = greater

        result = []
        for i in range(len(nums)):
            result.append(greaterMap[i])

        return result
