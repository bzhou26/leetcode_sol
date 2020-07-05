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


class Solution2(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        result = 0
        while x != 0 or y != 0:
            result += 1 if x % 2 != y % 2 else 0
            x = x >> 1
            y = y >> 1

        return result


class Solution3:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        distance = 0
        while num:
            if num & 1:
                distance += 1
            num >>= 1

        return distance