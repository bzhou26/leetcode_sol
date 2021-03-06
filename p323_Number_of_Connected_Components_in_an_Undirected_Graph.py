'''
- Leetcode problem: 323

- Difficulty: Medium

- Brief problem description:

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function
to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as
[1, 0] and thus will not appear together in edges.

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                self.dfs(i, visited, graph)
                count += 1
        return count

    def dfs(self, n, visited, graph):
        visited.add(n)
        for e in graph[n]:
            if e not in visited:
                self.dfs(e, visited, graph)
