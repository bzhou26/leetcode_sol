class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        binary_sum = x ^ y
        sum = 0
        while binary_sum > 0:
            sum += binary_sum % 2
            binary_sum //= 2
        return sum
        