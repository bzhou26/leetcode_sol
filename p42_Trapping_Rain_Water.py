'''
- Leetcode problem: 42

- Difficulty: Hard

- Brief problem description:

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

https://leetcode.com/problems/trapping-rain-water/

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

- Solution Summary:

Solution 1 is dp solution. Time O(n), Space O(n)
Solution 2 is two pointer solution. Time O(n), Space O(1)

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def trap(self, height: List[int]) -> int:
        leftWall = []
        rightWall = []
        leftMax = 0
        for i in range(len(height)):
            leftWall.append(leftMax)
            leftMax = max(leftMax, height[i])
        rightMax = 0
        for i in range(len(height) - 1, -1, -1):
            rightWall = [rightMax] + rightWall
            rightMax = max(rightMax, height[i])
        result = 0
        for i in range(len(height)):
            h = min(leftWall[i], rightWall[i])
            if height[i] < h:
                result += h - height[i]

        return result


class Solution2:
    def trap(self, height: List[int]) -> int:
        leftmax = 0
        rightmax = 0
        l = 0
        r = len(height) - 1
        result = 0
        while l < r:
            leftmax = max(height[l], leftmax)
            rightmax = max(height[r], rightmax)
            if leftmax < rightmax:
                result += leftmax - height[l]
                l += 1
            else:
                result += rightmax - height[r]
                r -= 1

        return result
