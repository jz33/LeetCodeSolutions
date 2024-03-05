'''
207. Course Schedule
https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take,
labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that
you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list) # [from course : [togo courses]]
        inDegrees = [0] * numCourses
        for toNode, fromNode in prerequisites:
            graph[fromNode].append(toNode);
            inDegrees[toNode] += 1

        courses = deque([node for node in range(numCourses) if inDegrees[node] == 0])
        coursesTaken = 0
        
        while courses:
            node = courses.popleft()
            coursesTaken += 1
            for toNode in graph[node]:
                inDegrees[toNode] -= 1
                if inDegrees[toNode] == 0 :
                    courses.append(toNode)

        return coursesTaken == numCourses
