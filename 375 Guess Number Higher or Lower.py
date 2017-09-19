'''
375 Guess Number Higher or Lower
https://leetcode.com/problems/guess-number-higher-or-lower-ii
'''
def getMoneyAmount(n):
    mat = [[0] * n] # row: buckle size; col: buckle index; starts from buckle 1
    # mat[x][y] means retrieve with buckle size x+1, index starts from y
    for i in xrange(1,n): # iterate row
        row = [0] * (n-i)
        for j in xrange(n-i): # iterate col
            # left or right, select max; total cut, select min
            m = j+1+mat[i-1][j+1] # left
            for k in xrange(j+1,j+i):
                m = min(m, max(mat[k-j-1][j],mat[j+i-k-1][k+1])+k+1)
            m = min(m, mat[i-1][j]+j+i+1) # right
            row[j] = m
        mat.append(row)
    return mat[n-1][0]
