/*
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
*/
function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    const graph: number[][] = new Array(numCourses); // [from course : [togo courses]]
    for (let i = 0; i < numCourses; i++) {
        graph[i] = [];
    }
    const indegrees = new Array(numCourses).fill(0);
    for (const [togoCourse, fromCourse] of prerequisites) {
        graph[fromCourse].push(togoCourse);
        indegrees[togoCourse]++;
    }

    // Topological sort
    let courses = Array.from(new Array(numCourses).keys()).filter(node => indegrees[node] === 0);
    let coursesTaken = 0;
    while (courses.length) {
        const newCourses: number[] = [];
        for (const node of courses) {
            coursesTaken++;
            for (const togo of graph[node]) {
                indegrees[togo]--;
                if (indegrees[togo] === 0) {
                    newCourses.push(togo);
                }
            }
        }
        courses = newCourses;
    }
    return coursesTaken === numCourses;
};
