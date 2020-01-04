'''
1136. Parallel Courses
https://leetcode.com/problems/parallel-courses/

There are N courses, labelled from 1 to N.

We are given relations[i] = [X, Y], representing a prerequisite relationship between course X and course Y:
course X has to be studied before course Y.

In one semester you can study any number of courses as long as you have studied all the prerequisites
for the course you are studying.

Return the minimum number of semesters needed to study all courses.
If there is no way to study all the courses, return -1.

Example 1:

Input: N = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: 
In the first semester, courses 1 and 2 are studied. In the second semester, course 3 is studied.

Example 2:

Input: N = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: 
No course can be studied because they depend on each other.

Note:

1 <= N <= 5000
1 <= relations.length <= 5000
relations[i][0] != relations[i][1]
There are no repeated relations in the input.
'''
class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        ranks = [0] * (N+1) # in-degress
        ranks[0] = -1 # ranks[0] not used
        for f,t in relations:
            graph[f].append(t)
            ranks[t] += 1
            
        queue = collections.deque([i for i in range(1, N+1) if ranks[i] == 0])
        total = 0
        level = 0
        while queue:
            total += len(queue)
            level += 1
            
            for _ in range(len(queue)):
                node = queue.popleft()
                for togo in graph[node]:
                    ranks[togo] -= 1
                    if ranks[togo] == 0:
                        queue.append(togo)
            
        return level if total == N else -1
