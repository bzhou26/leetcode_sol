'''
- Leetcode problem: 15

- Difficulty: Medium

- Brief problem description:

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets
in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

- Solution Summary:

Use dict to generate a 2 sum map, be careful for duplication result

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def threeSum(self, nums):
        sumDict = dict()
        result = []
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                sumValue = -(nums[i]+nums[j])
                sumResult = sumDict.get(sumValue)
                if not sumResult:
                    sumDict[sumValue] = [[i, j]]
                else:
                    sumResult.append([i, j])
                    sumDict[sumValue] = sumResult
        for k in range(len(nums)):
            sumList = sumDict.get(nums[k])
            if sumList:
                for l in sumList:
                    if k not in l:
                        picked = l[:]
                        picked.append(k)
                        oneSolution = [nums[picked[0]], nums[picked[1]], nums[picked[2]]]
                        exist = False
                        for e in result:
                            if set(e) == set(oneSolution):
                                exist = True
                        if not exist:
                            result.append(sorted(oneSolution))
        return list(result)
