def binaryRow(mat,up,dn,op):
    while up < dn:
        mid = (up + dn >> 1)
        if ('1' in mat[mid]) is op:
            dn = mid
        else:
            up = mid + 1
    return up

def binaryCol(mat,up,dn,lt,rt,op):
    while lt < rt:
        mid = (lt + rt >> 1)
        if any('1' == mat[x][mid] for x in xrange(up,dn)) is op:
            rt = mid
        else:
            lt = mid + 1
    return lt

def minArea(mat,i,j):
    upperRow = binaryRow(mat,0,i,True)
    lowerRow = binaryRow(mat,i+1,len(mat), False) # inclusive
    print upperRow, lowerRow
    leftCol = binaryCol(mat,upperRow, lowerRow, 0,j,True)
    rightCol = binaryCol(mat,upperRow, lowerRow, j+1,len(mat[i]),False)
    print leftCol, rightCol
    return (lowerRow - upperRow) * (rightCol - leftCol)
    
class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        return minArea(image,x,y)
        
