'''
- Leetcode problem: 207

- Difficulty: Medium

- Brief problem description:

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5

- Solution Summary:

Topological sort

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dag = defaultdict(list)
        in_degree = {}
        for p in prerequisites:
            in_degree[p[0]] = in_degree.get(p[0], 0) + 1
            dag[p[1]].append(p[0])

        zero_dq = deque()
        for i in range(numCourses):
            if not in_degree.get(i):
                zero_dq.append(i)

        ordered_course = []
        while zero_dq:
            course = zero_dq.popleft()
            ordered_course.append(course)

            nb = dag.get(course, [])
            for c in nb:
                in_degree[c] = in_degree.get(c) - 1
                if in_degree[c] == 0:
                    zero_dq.append(c)

        return len(ordered_course) == numCourses
