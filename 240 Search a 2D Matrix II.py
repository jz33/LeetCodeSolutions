import sys
'''
Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii/
'''
mat = None
tag = 0

'''
Binary search
If not present, return index that is
firstly larger than $tag
So max return index can be len(arr)
'''
def binary(arr, tag, lt, rt):
    while lt < rt :
        mid = (lt + rt >> 1)
        if arr[mid] == tag : return mid
        if arr[mid] < tag : lt = mid + 1
        else: rt = mid - 1

    # lt == rt
    if tag <= arr[lt]: return lt
    else: return lt + 1

'''
Binary Partition by row
O((lg n)^2)
'''
def partition(lt,rt,up,dn):
    if lt > rt or up > dn: return False
    if tag < mat[up][lt] or tag > mat[dn][rt] : return False
    
    # binary search mid row
    mid = (up + dn >> 1 )
    ind = binary(mat[mid],tag,lt,rt)
    if ind >= lt and ind <= rt and mat[mid][ind] == tag:
        print mid,ind
        return True
    
    # Notice why go to upper-right and lower-left only
    return partition(ind,rt,up,mid-1) or partition(lt,ind-1,mid+1,dn);

def searchMatrix(matrix,target):
    global mat, tag
    mat = matrix
    tag = target
    return partition(0,len(mat[0])-1,0,len(mat)-1)

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

print searchMatrix(matrix,int(sys.argv[1]))
