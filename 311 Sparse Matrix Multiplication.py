'''
Sparse Matrix Multiplication
https://leetcode.com/problems/sparse-matrix-multiplication/
'''
def dump(mat):
    for row in mat: print row

class Sparse(object):
    def __init__(self, R = -1, C = -1, val = [], row = [], col = []):
        self.R = R
        self.C = C
        self.val = val
        self.row = row
        self.col = col

    def fromDense(self,mat):
        self.R = len(mat)
        self.C = len(mat[0]) if self.R != 0 else 0
    
    def toDense(self):
        pass
    
    def __str__(self):
        print 'R: ', self.R
        print 'C: ', self.C
        print 'val: ', self.val
        print 'row: ', self.row
        print 'col: ', self.col
        return ''

class CSCD(Sparse):
    def __init__(self, R = -1, C = -1, val = [], row = [], col = []):
        super(CSCD,self).__init__(R,C,val,row,col)
    
    def fromDense(self,mat):
        super(CSCD,self).fromDense(mat)
        val,row,col = [],[],[]
        for i in xrange(self.R):
            for j in xrange(self.C):
                v = mat[i][j]
                if v != 0:
                    val.append(v)
                    row.append(i)
                    col.append(j)     
        self.val,self.row,self.col = val,row,col
    
    def toDense(self):
        mat = [[0 for _ in xrange(self.C)] for _ in xrange(self.R)]
        val,row,col = self.val,self.row,self.col
        for i,v in enumerate(val):
            mat[row[i]][col[i]] = v
        return mat

class CSR(Sparse):
    def __init__(self, R = -1, C = -1, val = [], row = [], col = []):
        assert len(row) - 1 == R
        super(CSR,self).__init__(R,C,val,row,col)

    def fromDense(self,mat):
        super(CSR,self).fromDense(mat)
        val,row,col = [],[0],[]
        for i in xrange(self.R):
            cc = row[-1]
            for j in xrange(self.C):
                v = mat[i][j]
                if v != 0:
                    val.append(v)
                    cc += 1
                    col.append(j)
            row.append(cc)       
        self.val,self.row,self.col = val,row,col
    
    def toDense(self):
        mat = [[0 for _ in xrange(self.C)] for _ in xrange(self.R)]
        val,row,col = self.val,self.row,self.col
        i = 0
        for ci in xrange(self.R):
            lt = row[ci]
            rt = row[ci+1]
            for _ in xrange(lt,rt):
                mat[ci][col[i]] = val[i]
                i += 1
        return mat
        
class CSC(Sparse):
    '''
    https://www.codatlas.com/github.com/apache/spark/7f74190/mllib/src/main/scala/org/apache/spark/mllib/linalg/Matrices.scala?line=488
    '''
    def __init__(self, R = -1, C = -1, val = [], row = [], col = []):
        assert len(col) - 1 == C
        super(CSC,self).__init__(R,C,val,row,col) 
        
    def fromDense(self,mat):
        super(CSC,self).fromDense(mat)
        val,row,col = [],[],[0]
        for i in xrange(self.C):
            cc = col[-1]
            for j in xrange(self.R):
                v = mat[j][i]
                if v != 0:
                    val.append(v)
                    row.append(j)
                    cc += 1
            col.append(cc)       
        self.val,self.row,self.col = val,row,col
    
    def toDense(self):
        mat = [[0 for _ in xrange(self.C)] for _ in xrange(self.R)]
        val,row,col = self.val,self.row,self.col
        i = 0
        for ci in xrange(self.C):
            lt = col[ci]
            rt = col[ci+1]
            for _ in xrange(lt,rt):
                mat[row[i]][ci] = val[i]
                i += 1
        return mat
  
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        '''
        CSR * CSC = CSCD
        '''
        csr = CSR()
        csr.fromDense(A)
        csc = CSC()
        csc.fromDense(B)        
        # print csr
        # print csc
        
        cscd_val,cscd_row,cscd_col = [],[],[]
        for i in xrange(len(csr.row)-1):
            ll, lr = csr.row[i], csr.row[i+1]
            for j in xrange(len(csc.col)-1):
                rl, rr = csc.col[j],csc.col[j+1]
                x = ll
                y = rl
                t = 0
                while x < lr and y < rr:
                    xv = csr.col[x]
                    yv = csc.row[y]
                    if xv < yv:
                        x += 1
                    elif xv > yv:
                        y += 1
                    else:
                        t += csr.val[x] * csc.val[y]
                        x += 1
                        y += 1
                if t != 0:
                    cscd_val.append(t)
                    cscd_row.append(i)
                    cscd_col.append(j)

        R = len(A)
        C = len(B[0])
        obj = CSCD(R,C,cscd_val,cscd_row,cscd_col)
        return obj.toDense()
            
sol = Solution()
A = [
  [ 1, 2, 3, 4, 5],
  [-1,-2,-3,-4,-5]
]

B = [
  [1],
  [1],
  [1],
  [1],
  [1]
]  

C = sol.multiply(A,B)
dump(C)
