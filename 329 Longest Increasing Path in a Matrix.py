'''
Longest Increasing Path in a Matrix
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
Have to convert to Java to pass extreme test case
'''
def longestIncreasingPath(mat):
    R = len(mat)
    if R == 0 : return 0
    C = len(mat[0])
    if C == 0 : return 0
    ref = [[0 for _ in xrange(C)] for _ in xrange(R)]
    
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    maxDepth = 1
    
    for i in xrange(R):
        for j in xrange(C):
            # start bfs from unvisited node
            if ref[i][j] == 0:
                queue = [(i,j)]
                depth = 1
                while len(queue) > 0:
                    depth += 1
                    for _ in xrange(len(queue)):
                        (i1,j1) = queue.pop(0)
                        for dir in directions:
                            i2 = i1 + dir[0]
                            if i2 > -1 and i2 < R:
                                j2 = j1 + dir[1]
                                if j2 > -1 and j2 < C:
                                    if mat[i2][j2] > mat[i1][j1] and depth > ref[i2][j2]:
                                        ref[i2][j2] = depth
                                        maxDepth = max(maxDepth,depth)
                                        queue.append((i2,j2))
                                        
    return maxDepth
