'''
- Leetcode problem: 1306

- Difficulty: Medium

- Brief problem description:

Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at
index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.



Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation:
All possible ways to reach at index 3 with value 0 are:
index 5 -> index 4 -> index 1 -> index 3
index 5 -> index 6 -> index 4 -> index 1 -> index 3
Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true
Explanation:
One possible way to reach at index 3 with value 0 is:
index 0 -> index 4 -> index 1 -> index 3
Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.


Constraints:

1 <= arr.length <= 5 * 10^4
0 <= arr[i] < arr.length
0 <= start < arr.length

- Solution Summary:

Typical backtracking solution

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def canReach(self, arr, start):
        return self.reachCheck(arr, set(), start)

    def reachCheck(self, arr, visited, i):
        if i < 0 or i > len(arr) - 1 or (i in visited and arr[i] != 0):
            return False
        if arr[i] == 0:
            return True
        visited.add(i)
        result = self.reachCheck(arr, visited, i - arr[i])
        if not result:
            result = self.reachCheck(arr, visited, i + arr[i])
        visited.remove(i)

        return result


if __name__ == "__main__":
    solution = Solution()
    testList = [4,2,3,0,3,1,2]
    print(solution.canReach(testList, 5))