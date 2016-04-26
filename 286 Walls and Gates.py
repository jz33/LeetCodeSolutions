import sys
from collections import deque
'''
Walls and Gates
https://leetcode.com/problems/walls-and-gates/
'''
WALL = -1
GATE = 0
INF = 2147483647
R = 0
C = 0

def mark(mat,x,y):
    dq = deque()
    dq.append((x,y,0))
    while len(dq) > 0:
        x,y,d = dq.popleft()
        mat[x][y] = d
        if x + 1 <  R and mat[x+1][y] != WALL and mat[x+1][y] > d+1:
            dq.append((x+1,y,d+1))
        if x - 1 > -1 and mat[x-1][y] != WALL and mat[x-1][y] > d+1:
            dq.append((x-1,y,d+1))
        if y + 1 < C  and mat[x][y+1] != WALL and mat[x][y+1] > d+1:
            dq.append((x,y+1,d+1))
        if y - 1 > -1 and mat[x][y-1] != WALL and mat[x][y-1] > d+1:
            dq.append((x,y-1,d+1))

def solve(mat):   
    global R,C
    R = len(mat)
    if R == 0: return
    C = len(mat[0])

    for i in xrange(R):
        for j in xrange(C):
            if mat[i][j] == GATE:
                mark(mat,i,j)           
                
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        solve(rooms)
'''
rooms = [
    [INF,  -1,  0,  INF],
    [INF, INF, INF,  -1],
    [INF,  -1, INF,  -1],
    [0,    -1, INF, INF]
]
'''
rooms = [
    [0,  INF, INF,   0,  -1,  -1, 0,    0,   0,  -1,  -1,   0, INF, INF],
    [INF, -1, INF,  -1, INF,   0, -1, INF,  -1, INF, INF,  -1,  -1, INF],
    [0,    0,  -1, INF,  -1, INF, -1,  -1, INF,   0,   0, INF,   0, INF],
    [-1,   0, INF,  -1,   0,   0, -1, INF,   0, INF,   0,  -1,   0,  -1]
]  
sol = Solution()
sol.wallsAndGates(rooms)
for row in rooms:
    for c in row:
        if c == INF:
            sys.stdout.write('{0: <5}'.format('INF'))
        else:
            sys.stdout.write('{0: <5}'.format(str(c)))
    sys.stdout.write('\n')
