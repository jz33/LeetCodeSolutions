from heapq import heappush, heappop
'''
378 Kth Smallest Element in a Sorted Matrix
https://leetcode.com/problems/
'''
def kthSmallest(mat, k):
    '''
    The distance from this point to top-left is less than k
    There will be better filter before put into heap
    '''
    n = len(mat)
    h = []
    for i in xrange(min(k+1,n)):
        for j in xrange(min(k-i,n)):
            heappush(h,mat[i][j])
    
    print h
    for i in xrange(k-1):
        heappop(h)
    return heappop(h)

mat = [\
[1, 5, 9],\
[10,11,13],\
[12,13,15],\
]

# mat = [\
# [2,3,8,11,15],\
# [4,8,12,15,18],\
# [5,8,17,20,22],\
# [6,12,18,20,25],\
# [9,14,21,24,25],\
# ]

for i in xrange(1,len(mat)**2+1):
    print kthSmallest(mat,i)
