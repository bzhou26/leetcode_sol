'''
- Leetcode problem: 934

- Difficulty: Medium

- Brief problem description:

In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not
connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)



Example 1:

Input: A = [[0,1],[1,0]]
Output: 1
Example 2:

Input: A = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1


Constraints:

2 <= A.length == A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1

- Solution Summary:

DFS to find the island and flip all to 2, add the edge points to deque.
BFS to find the shortest steps

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        dircts = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        found = False
        dq = deque()
        for i in range(len(A)):
            if found:
                break
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    self.dfs(i, j, A, dq, dircts)
                    found = True
                    break
        step = 0
        visited = set()
        while dq:
            n = len(dq)
            for i in range(n):
                x, y = dq.popleft()
                A[x][y] = 3
                for dx, dy in dircts:
                    new_x = x + dx
                    new_y = y + dy
                    if 0 <= new_x < len(A) and 0 <= new_y < len(A[0]) and (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        if A[new_x][new_y] == 1:
                            return step
                        if A[new_x][new_y] == 0:
                            dq.append((new_x, new_y))
            step += 1
        return step

    def dfs(self, x, y, A, dq, dircts):
        A[x][y] = 2
        count = 0
        for dx, dy in dircts:
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < len(A) and 0 <= new_y < len(A[0]):
                if A[new_x][new_y] == 1:
                    count += 1
                    self.dfs(new_x, new_y, A, dq, dircts)
            else:
                count += 1
        if count != 4:
            dq.append((x, y))
