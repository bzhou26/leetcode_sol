'''
- Leetcode problem: 210

- Difficulty: Medium

- Brief problem description:

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

- Solution Summary:

Topological sort

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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

        if len(ordered_course) == numCourses:
            return ordered_course
        else:
            return []
