'''
- Leetcode problem: 1060

- Difficulty: Medium

- Brief problem description:

    Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation:
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation:
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation:
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.

Note:

1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8

- Solution Summary:

[4, 7, 10, 13] k = 3

missing number = nums[i] - nums[0] - i

1. Binary Search to find the missing number.

7: 2 missing number before it
10: 4 missing number before it
So result is 7 + (k - missing number at 7)
Edge case: if k is larger enough that it's not contained in the list, we can return it directly.

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def missingElement(self, nums, k) -> int:
        if (nums[-1] - nums[0] - (len(nums) - 1)) < k:
            return k - (nums[-1] - nums[0] - (len(nums) - 1)) + nums[-1]
        low, high = 0, len(nums) - 1
        while low < high - 1:
            mid = (high + low) // 2
            if nums[mid] - nums[0] - mid < k:
                low = mid
            else:
                high = mid
        return k - (nums[low] - nums[0] - low) + nums[low]


if __name__ == "__main__":
    solution = Solution()
    testList = [1, 2, 4]
    print(solution.missingElement(testList, 3))
