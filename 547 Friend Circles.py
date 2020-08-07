'''
547. Friend Circles
https://leetcode.com/problems/friend-circles/

There are N students in a class. Some of them are friends, while some are not.
Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C,
then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class.
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.
And you have to output the total number of friend circles among all the students.

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
class UnionFind:
    def __init__(self, count: int):
        self.tree = list(range(count))

    def find(self, node):
        tree = self.tree
        if tree[node] != node:
            tree[node] = self.find(tree[node])
        return tree[node]
    
    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra != rb:
            self.tree[ra] = rb

    def rootCount(self) -> int:
        return sum(k == v for k, v in enumerate(self.tree))

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        count = len(M)
        if not count:
            return 0
        
        graph = UnionFind(count)
        for i in range(count):
            for j in range(i + 1, count):
                if M[i][j] == 1:
                    graph.union(i, j)
        
        return graph.rootCount()
