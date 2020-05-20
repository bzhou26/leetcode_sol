'''
- Leetcode problem: 763

- Difficulty: Medium

- Brief problem description:

    A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that
    each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.

- Solution Summary:

Find all last appearance of characters, then go thought the string. When current position equals to the max end
position, then append to the result

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = dict()
        for i in range(len(S) - 1, -1, -1):
            if not last.get(S[i]):
                last[S[i]] = i
        start = end = current = 0
        result = []
        while current < len(S):
            end = max(last.get(S[current], current), end)
            if current == end:
                result.append(end - start + 1)
                start = end = current + 1
            current += 1
        return result


if __name__ == "__main__":
    solution = Solution()
    testStr = 'ababcbacadefegdehijhklij'
    print(solution.partitionLabels(testStr))