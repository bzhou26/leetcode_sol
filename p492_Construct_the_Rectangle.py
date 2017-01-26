class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        for i in range(int(pow(area, 0.5)), 0, -1):
            if area % i == 0:
                return [area // i, i]