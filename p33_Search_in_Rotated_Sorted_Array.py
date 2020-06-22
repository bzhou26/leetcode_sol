'''
- Leetcode problem: 33

- Difficulty: Medium

- Brief problem description:

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1
        s = nums[0]
        e = nums[-1]
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2

            if target == nums[mid]:
                return mid
            if nums[mid] >= s:
                if nums[mid] > target and target >= s:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= e:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


if __name__ == "__main__":
    solution = Solution()
    testList = [1, 3]
    print(solution.search(testList, 3))
