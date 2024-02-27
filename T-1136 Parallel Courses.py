'''
1136. Parallel Courses
https://leetcode.com/problems/parallel-courses/

You are given an integer n, which indicates that there are n courses labeled from 1 to n.
You are also given an array relations where relations[i] = [prevCoursei, nextCoursei],
representing a prerequisite relationship between course prevCoursei and course nextCoursei:
course prevCoursei has to be taken before course nextCoursei.

In one semester, you can take any number of courses as long as you have taken all the prerequisites
in the previous semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses.
If there is no way to take all the courses, return -1.

Example 1:

Input: n = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 1 and 2.
In the second semester, you can take course 3.

Example 2:

Input: n = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: No course can be studied because they are prerequisites of each other.

Constraints:
    1 <= n <= 5000
    1 <= relations.length <= 5000
    relations[i].length == 2
    1 <= prevCoursei, nextCoursei <= n
    prevCoursei != nextCoursei
    All the pairs [prevCoursei, nextCoursei] are unique.
'''
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegrees = [0] * n
        for fromNode, toNode in relations:
            graph[fromNode-1].append(toNode-1)
            indegrees[toNode-1] += 1
            
        queue = deque([i for i in range(n) if indegrees[i] == 0])
        totalCourseTaken = 0
        semesters = 0
        while queue:
            totalCourseTaken += len(queue)
            semesters += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for toNode in graph[node]:
                    indegrees[toNode] -= 1
                    if indegrees[toNode] == 0:
                        queue.append(toNode)
        return semesters if totalCourseTaken == n else -1
