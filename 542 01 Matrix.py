'''
https://leetcode.com/problems/01-matrix
DFS will timeout
Use 2 pass DP
'''
def updateFromFourDirections(src,dis,R,C,INF,i,j):
    if src[i][j] == 0:
        dis[i][j] = 0
    else:
        if i+1 < R and dis[i+1][j] != INF and dis[i][j] > dis[i+1][j]+1:
            dis[i][j] = dis[i+1][j]+1
        if i-1 >-1 and dis[i-1][j] != INF and dis[i][j] > dis[i-1][j]+1:
            dis[i][j] = dis[i-1][j]+1
        if j+1 < C and dis[i][j+1] != INF and dis[i][j] > dis[i][j+1]+1:
            dis[i][j] = dis[i][j+1]+1
        if j-1 >-1 and dis[i][j-1] != INF and dis[i][j] > dis[i][j-1]+1:
            dis[i][j] = dis[i][j-1]+1

def updateMatrix(src):
    R = len(src)
    C = len(src[0])
    INF = R*C+1
    dis = [[INF for _ in xrange(C)] for _ in xrange(R)]

    # up-down pass
    for i in xrange(R):
        for j in xrange(C):
            updateFromFourDirections(src,dis,R,C,INF,i,j)
            printMat(dis)
    
    # reverse pass  
    for i in xrange(R-1,-1,-1):
        for j in xrange(C-1,-1,-1):
            updateFromFourDirections(src,dis,R,C,INF,i,j)
            printMat(dis)

    return dis

def printMat(src):
    for r in src:
        print r
    print

mat = [\
[1,1,0],\
[1,1,1],\
[1,1,1],\
]

printMat(updateMatrix(mat))
