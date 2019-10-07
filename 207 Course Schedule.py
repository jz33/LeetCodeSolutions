'''
207 Course Schedule
https://leetcode.com/problems/course-schedule/

There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
'''
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)] # vertice : [togo vertices]
        ranks = [0] * numCourses # income degree

        for edge in prerequisites:
            a = edge[0]
            b = edge[1]
            # Need to take a before b, then edge is b -> a
            graph[b].append(a)
            ranks[a] += 1

        # Sort
        queue = deque([i for i, r in enumerate(ranks) if r == 0])

        reachedCourse = 0
        while queue:
            node = queue.popleft()
            reachedCourse += 1
            for togo in graph[node]:
                if ranks[togo] == 1:
                    queue.append(togo)
                ranks[togo] -= 1
            
        return reachedCourse == numCourses
