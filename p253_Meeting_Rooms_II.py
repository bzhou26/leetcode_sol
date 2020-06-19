'''
- Leetcode problem: 253

- Difficulty: Medium

- Brief problem description:

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the
minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method
signature.

- Solution Summary:

Priority queue (heap) solution

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        if len(intervals) == 0:
            return 0
        count = 0
        timeH = []

        for inter in intervals:
            if len(timeH) == 0:
                count += 1
            else:
                if inter[0] < timeH[0]:
                    count += 1
                else:
                    heapq.heappop(timeH)
            heapq.heappush(timeH, inter[1])

        return count
