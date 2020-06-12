'''
- Leetcode problem: 675

- Difficulty: Hard

- Brief problem description:

You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
In one step you can walk in any of the four directions top, bottom, left and right also when standing in a point which is a tree you can decide whether or not to cut off the tree.

You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:

Input:
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6


Example 2:

Input:
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1


Example 3:

Input:
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.


Constraints:

1 <= forest.length <= 50
1 <= forest[i].length <= 50
0 <= forest[i][j] <= 10^9

- Solution Summary:

1. Sort the trees by tree height
2. Calculate the shortest path by BFS

Time Complexity: O((RC)^2)
Space Complexity: O(R*C)

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        treeList = []
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] > 1:
                    treeList.append((forest[i][j], (i, j)))
        treeList.sort(key=lambda x: x[0])

        totalDist = 0
        startPoint = (0, 0)
        for tree in treeList:
            dist = self.shortestPath(forest, startPoint[0], startPoint[1], tree[1][0], tree[1][1])
            if dist == -1:
                return -1
            else:
                totalDist += dist
            startPoint = (tree[1][0], tree[1][1])

        return totalDist

    def shortestPath(self, forest, sx, sy, tx, ty) -> int:
        if sx == tx and sy == ty:
            return 0

        directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visited = set()
        dq = deque()
        dq.append((sx, sy))

        step = 0
        while dq:
            n = len(dq)
            step += 1
            for i in range(n):
                x, y = dq.popleft()
                for dx, dy in directs:
                    newX = x + dx
                    newY = y + dy
                    if newX == tx and newY == ty:
                        return step
                    elif 0 <= newX < len(forest) and 0 <= newY < len(forest[0]) and (newX, newY) not in visited and \
                            forest[newX][newY] != 0:
                        visited.add((newX, newY))
                        dq.append((newX, newY))

        return -1
