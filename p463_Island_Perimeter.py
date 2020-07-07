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


class Solution2:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total = 0
        direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cur = 4
                    for dx, dy in direct:
                        new_x = i + dx
                        new_y = j + dy
                        if  0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                            if grid[new_x][new_y] == 1:
                                cur -= 1
                    total += cur
        return total
