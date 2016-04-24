from heapq import heappush, heappop
'''
218 The Skyline Problem
https://leetcode.com/problems/the-skyline-problem/
'''
def getSkyline(bs):
    '''
    @bs: buildings, [[left,right,height]...]
    '''
    n = len(bs)
    skyline = []
    heap = [] # (-height, -right)
    i = 0
    while i < n or len(heap) > 0:
        if len(heap) == 0 or i < n and bs[i][0] <= heap[0][1]:
            ind = bs[i][0]
            while i < n and bs[i][0] == ind:
                heappush(heap, (-bs[i][2], bs[i][1]))
                i += 1
        else:
            ind = heap[0][1]
            while len(heap) > 0 and heap[0][1] <= ind:
                heappop(heap)

        height = -heap[0][0] if len(heap) > 0 else 0
        if len(skyline) == 0 or height != skyline[-1][1]:
            skyline.append([ind, height])
    return skyline


buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
#buildings = [[1,2,1],[1,2,2]]
for pair in getSkyline(buildings):
    print pair,
print
