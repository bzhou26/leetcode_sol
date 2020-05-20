class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sub = 0
        sub = 0
        for i in nums:
           if i == 1: 
               sub += 1
               max_sub = max(sub, max_sub)
           else:
               sub = 0
        return max_sub