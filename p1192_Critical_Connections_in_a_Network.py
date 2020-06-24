'''
- Leetcode problem: 1192

- Difficulty: Hard

- Brief problem description:

There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where
connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly
or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.



Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.


Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.

- Solution Summary:

Tarjan algo:
https://www.acwing.com/blog/content/376/

- Used Resources:

--- Bo Zhou
'''


import collections
class Solution:
    def criticalConnections(self, n: int, connections):
        graph = collections.defaultdict(list)
        for c in connections:
            graph[c[0]].append(c[1])
            graph[c[1]].append(c[0])

        i = 0
        index = [0 for i in range(n)]
        low = [-1 for i in range(n)]

        result = []

        def dfs(cur, pre):
            nonlocal i
            index[cur] = i
            low[cur] = i
            i += 1
            for dst in graph[cur]:
                if dst == pre:
                    continue
                if low[dst] == -1:
                    dfs(dst, cur)
                    if index[dst] <= low[dst]:
                        result.append((cur, dst))
                low[cur] = min(low[cur], low[dst])

        dfs(0, -1)
        return result


if __name__ == "__main__":
    solution = Solution()
    testList = [[0,1],[1,2],[2,0],[1,3]]
    print(solution.criticalConnections(4, testList))
