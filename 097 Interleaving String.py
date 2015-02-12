'''
97 Interleaving String
https://oj.leetcode.com/problems/interleaving-string/
Dynamic Programming
'''
def isInterleaving(t,s0,s1):
    n0 = len(s0)
    n1 = len(s1)
    if len(t) == 0 and n0 == 0 and n1 == 0: return True
    if len(t) != n0 + n1: return False

    mat = [[0 for t1 in range(n1+1)] for t0 in range(n0+1)]
    mat[0][0] = 1

    for i in range(0,n0):
        if s0[i] == t[i] and mat[i][0] == 1: mat[i+1][0] = 1
    for i in range(0,n1):
        if s1[i] == t[i] and mat[0][i] == 1: mat[0][i+1] = 1
    for i in range(0,n0):
        for j in range(0,n1):
            mat[i+1][j+1] = 1 if \
                            mat[i][j+1] == 1 and s0[i]==t[i+j+1] or \
                            mat[i+1][j] == 1 and s1[j]==t[i+j+1] \
                            else 0
    for row in mat:
        print row
        
    return mat[n0][n1]

def main():
    s0 = r'aabcc'
    s1 = r'dbbca'
    t0 = r'aadbbcbcac'
    t1 = r'aadbbbaccc'
    print isInterleaving(t0,s0,s1)
    print isInterleaving(t1,s0,s1)
    
if __name__ == "__main__":
    main()
