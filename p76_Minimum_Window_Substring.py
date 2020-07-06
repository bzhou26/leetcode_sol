'''
- Leetcode problem: 76

- Difficulty: Hard

- Brief problem description:

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in
complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = {}
        for c in t:
            tmap[c] = tmap.get(c, 0) + 1

        l = 0
        r = 0
        moveLeft = False
        cmap = {}

        shortest = float('inf')
        shortRet = ''

        while r < len(s):
            if moveLeft:
                if r - l < shortest:
                    shortest = r - l
                    shortRet = s[l:r + 1]

                if tmap.get(s[l]) is not None:
                    if cmap.get(s[l]) > 1:
                        cmap[s[l]] = cmap.get(s[l]) - 1
                    else:
                        del cmap[s[l]]
                    if cmap.get(s[l], 0) < tmap[s[l]]:
                        moveLeft = False
                l += 1
                if not moveLeft:
                    r += 1
            else:
                if tmap.get(s[r]) is not None:
                    cmap[s[r]] = cmap.get(s[r], 0) + 1
                if self.checkValid(cmap, tmap):
                    moveLeft = True
                if not moveLeft:
                    r += 1

        return shortRet

    def checkValid(self, cmap, tmap):
        if len(cmap) != len(tmap):
            return False
        for k, v in tmap.items():
            if cmap.get(k, 0) < v:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    testList = "ADOBECODEBANC"
    print(solution.minWindow(testList, "ABC"))
