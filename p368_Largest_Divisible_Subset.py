'''
- Leetcode problem: 368

- Difficulty: Medium

- Brief problem description:

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]

- Solution Summary:

DP solution, O(n**2) time, O(n**2) space. The space can be improved to O(n) because we only need to calculate one number
 for each previous set

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        nums.sort()
        dp = [[nums[0]]]
        result = []
        for i in range(1, len(nums)):
            curSet = []
            for j in range(i - 1, -1, -1):
                prevSet = dp[j]
                if nums[i] % prevSet[-1] == 0:
                    if len(prevSet) > len(curSet):
                        curSet = prevSet[:]
            curSet.append(nums[i])
            dp.append(curSet)

            if len(result) < len(dp[i]):
                result = dp[i]
        return result
