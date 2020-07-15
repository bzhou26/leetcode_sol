'''
- Leetcode problem: 1344

- Difficulty: Medium

- Brief problem description:

Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.



Example 1:



Input: hour = 12, minutes = 30
Output: 165
Example 2:



Input: hour = 3, minutes = 30
Output: 75
Example 3:



Input: hour = 3, minutes = 15
Output: 7.5
Example 4:

Input: hour = 4, minutes = 50
Output: 155
Example 5:

Input: hour = 12, minutes = 0
Output: 0


Constraints:

1 <= hour <= 12
0 <= minutes <= 59
Answers within 10^-5 of the actual value will be accepted as correct.

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h_degree = (hour * (360 / 12)) + ((minutes / 60) * (360 / 12))
        if h_degree > 360:
            h_degree -= 360

        m_degree = minutes / 60 * 360

        result = 0
        if h_degree > m_degree:
            result = h_degree - m_degree
        else:
            result = m_degree - h_degree

        if result > 180:
            result = 360 - result

        return result
