'''
Surrounded Regions
https://leetcode.com/problems/surrounded-regions/
'''
R = 0
C = 0
def mark(mat,pt):
    dq = []
    dq.append(pt)
    while len(dq) > 0:
        (x,y) = dq.pop()
        mat[x][y] = 'V'
        if x + 1 <  R and mat[x+1][y] == 'O':
            dq.append((x+1,y))
        if x - 1 > -1 and mat[x-1][y] == 'O':
            dq.append((x-1,y))
        if y + 1 < C  and mat[x][y+1] == 'O':
            dq.append((x,y+1))
        if y - 1 > -1 and mat[x][y-1] == 'O':
            dq.append((x,y-1))

def solve(mat):   
    global R,C
    R = len(mat)
    if R == 0: return
    C = len(mat[0])
    
    # check perimeter only
    for i in xrange(0,R):
        if mat[i][0] == 'O':
            mark(mat,(i,0))
        if mat[i][C-1] == 'O':
            mark(mat,(i,C-1))            
    for i in xrange(1,C-1):
        if mat[0][i] == 'O':
            mark(mat,(0,i))
        if mat[R-1][i] == 'O':
            mark(mat,(R-1,i))
            
    # after work
    for i in xrange(0,R):
        for j in xrange(0,C):
            if mat[i][j] == 'O':
                mat[i][j] = 'X'
            elif mat[i][j] == 'V':
                mat[i][j] = 'O'
    
def preWork(board):
    mat = []
    for row in board:
        mat.append(list(row))
    solve(mat)
    return mat
    
board = [
    "XOOOOOOOOOOOOOOOOOOO",
    "OXOOOOXOOOOOOOOOOOXX",
    "OOOOOOOOXOOOOOOOOOOX",
    "OOXOOOOOOOOOOOOOOOXO",
    "OOOOOXOOOOXOOOOOXOOX",
    "XOOOXOOOOOXOXOXOXOXO",
    "OOOOXOOXOOOOOXOOXOOO",
    "XOOOXXXOXOOOOXXOXOOO",
    "OOOOOXXXXOOOOXOOXOOO",
    "XOOOOXOOOOOOXXOOXOOX",
    "OOOOOOOOOOXOOXOOOXOX",
    "OOOOXOXOOXXOOOOOXOOO",
    "XXOOOOOXOOOOOOOOOOOO",
    "OXOXOOOXOXOOOXOXOXOO",
    "OOXOOOOOOOXOOOOOXOXO",
    "XXOOOOOOOOXOXXOOOXOO",
    "OOXOOOOOOOXOOXOXOXOO",
    "OOOXOOOOOXXXOOXOOOXO",
    "OOOOOOOOOOOOOOOOOOOO",
    "XOOOOXOOOXXOOXOXOXOO"
    ]
    
mat = preWork(board)
for row in mat:
    print row
