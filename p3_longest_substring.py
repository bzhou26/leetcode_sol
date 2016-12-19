class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        left = 0
        right = 0
        maxSet = set()
        while left < len(s) and right < len(s):
            if s[right] not in maxSet:
                maxSet.add(s[right])
                right += 1
                ans = max(ans, right - left)
            else:
                maxSet.remove(s[left])
                left += 1
        return ans