class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = {}
        for num in nums:
            result[num] = result.get(num, 0) + 1
        for key, val in result.items():
            if val == 1:
                return key
