'''
547. Friend Circles
https://leetcode.com/problems/friend-circles/

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:

Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
'''
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        '''
        A classic Union Find implementation
        Simply count root or connected graph
        '''
        count = len(M)
        if count == 0:
            return 0
    
        # The node : root graph.
        # '-1' means no root is set yet, aka itself is root
        graph = [-1] * count
    
        def getRoot(i):
            # Not if graph[i] != -1
            while graph[i] != -1:
                i = graph[i]
            return i
              
        # Find all "edges", avoid duplicated matrix iteration
        for i in range(count):
            for j in range(i + 1, count):
                if M[i][j] == 1:
                    ri = getRoot(i)
                    rj = getRoot(j)
                    
                    # Point bigger indexed node to smaller indexed node
                    if ri != rj:
                        if ri < rj:
                            graph[rj] = ri
                        else:
                            graph[ri] = rj
        
        # Count all roots
        return sum(1 for node in graph if node == -1)
