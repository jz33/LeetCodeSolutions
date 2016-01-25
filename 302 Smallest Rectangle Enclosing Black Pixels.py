'''
Smallest Rectangle Enclosing Black Pixels
https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/
'''
def lower_bound_row(mat,up,dn):
    '''
    Find first row which has '1'
    '''
    while up < dn:
        mid = (up + dn >> 1)
        if '1' in mat[mid]:
            dn = mid - 1
        else:
            up = mid + 1
    return up if '1' in mat[up] else up + 1

def upper_bound_row(mat,up,dn):
    '''
    Find first row which has NO '1'
    '''
    while up < dn:
        mid = (up + dn >> 1)
        if '1' not in mat[mid]:
            dn = mid - 1
        else:
            up = mid + 1
    return dn if '1' not in mat[dn] else dn + 1

def lower_bound_col(mat,up,dn,lt,rt):
    '''
    Find left most column which has '1'
    '''
    while lt < rt:
        mid = (lt + rt >> 1)
        if any('1' == mat[x][mid] for x in xrange(up,dn)) is True:
            rt = mid - 1
        else:
            lt = mid + 1
    return lt if any('1' == mat[x][lt] for x in xrange(up,dn)) is True else lt + 1

def upper_bound_col(mat,up,dn,lt,rt):
    '''
    Find left most column which has NO '1'
    '''
    while lt < rt:
        mid = (lt + rt >> 1)
        if any('1' == mat[x][mid] for x in xrange(up,dn)) is False:
            rt = mid - 1
        else:
            lt = mid + 1
    return lt if any('1' == mat[x][lt] for x in xrange(up,dn)) is False else lt + 1

def minArea(mat,i,j):
    upperRow = lower_bound_row(mat,0,i)
    lowerRow = upper_bound_row(mat,i,len(mat)-1)
    print upperRow, lowerRow
    leftCol  = lower_bound_col(mat,upperRow,lowerRow,0,j)
    rightCol = upper_bound_col(mat,upperRow,lowerRow,j,len(mat[i])-1)
    print leftCol, rightCol
    return (lowerRow - upperRow) * (rightCol - leftCol)
