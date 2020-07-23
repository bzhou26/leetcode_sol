'''
- Leetcode problem: 260

- Difficulty: Medium

- Brief problem description:

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly
twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

Constraints:

1 <= n <= 1000

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        result = []
        for k, v in d.items():
            if v == 1:
                result.append(k)
        return result
