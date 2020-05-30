'''
- Leetcode problem: 200

- Difficulty: Medium

- Brief problem description:

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and
is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

- Solution Summary:

Once you meet a 1, flip it to 0 and do a BFS, flip all related 1 to 0

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.removeIslandEdges(grid, i, j)
        return count

    def removeIslandEdges(self, grid, x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != "1":
            return
        grid[x][y] = "0"
        self.removeIslandEdges(grid, x - 1, y)
        self.removeIslandEdges(grid, x + 1, y)
        self.removeIslandEdges(grid, x, y - 1)
        self.removeIslandEdges(grid, x, y + 1)