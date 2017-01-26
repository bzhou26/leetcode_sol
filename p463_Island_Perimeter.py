class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum = 0
        for w in range(len(grid)):
            for h in range(len(grid[0])):
                if grid[w][h] == 1: add_length = 4
                else: continue
                if w != 0 and grid[w - 1][h] == 1: add_length -= 2
                if h != 0 and grid[w][h - 1] == 1: add_length -= 2
                sum += add_length
        return sum
                