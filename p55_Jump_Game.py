'''
- Leetcode problem: 55

- Difficulty: Medium

- Brief problem description:

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible
to reach the last index.


Constraints:

1 <= nums.length <= 3 * 10^4
0 <= nums[i][j] <= 10^5

- Solution Summary:

DP with memory, reduce time from O(n**2) to O(n)

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        dp = [False for i in range(len(nums))]

        dp[-1] = True

        lastTruePos = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= lastTruePos:
                dp[i] = True
                lastTruePos = i

        return dp[0]


if __name__ == "__main__":
    solution = Solution()
    testList = [2,3,1,1,4]
    print(solution.canJump(testList))