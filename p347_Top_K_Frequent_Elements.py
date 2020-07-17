'''
- Leetcode problem: 347

- Difficulty: Medium

- Brief problem description:

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        od = collections.OrderedDict(sorted(d.items(), key=lambda t: t[1], reverse=True))
        result = []
        i = 0
        for key, v in od.items():
            result.append(key)
            i += 1
            if i == k:
                break

        return result