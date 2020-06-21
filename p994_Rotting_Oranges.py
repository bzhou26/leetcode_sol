class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        result = 0
        dq = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    dq.append((i, j))
        result = max(result, self.bfs(dq, grid))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return result

    def bfs(self, dq, grid):
        directs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        count = -1
        while dq:
            count += 1
            n = len(dq)
            dq2 = deque()
            for i in range(n):
                curx, cury = dq.popleft()
                grid[curx][cury] = -1
                dq2.append((curx, cury))
            while dq2:
                curx, cury = dq2.popleft()
                for dx, dy in directs:
                    newx = curx + dx
                    newy = cury + dy
                    if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]) and grid[newx][newy] == 1:
                        dq.append((newx, newy))

        return count


if __name__ == "__main__":
    solution = Solution()
    testList = [[2,2],[1,1],[0,0],[2,0]]
    print(solution.orangesRotting(testList))
