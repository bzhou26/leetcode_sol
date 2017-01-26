class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [i for i in range(1, len(nums) + 1)]
        for i in range(len(nums)):
            result[nums[i] - 1] = -1
        result[:] = (v for v in result if v != -1)
        return result