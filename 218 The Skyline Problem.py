from heapq import heappush, heappop
'''
218 The Skyline Problem
https://leetcode.com/problems/the-skyline-problem/
'''
from heapq import heappush, heappop

def getSkyline(bs):
    '''
    @bs: buildings, [[left,right,height]...]
    @output: [[bound,height]...]
    '''
    n = len(bs)
    skyline = []
    heap = [] # (-height, right)
    i = 0
    while i < n or len(heap) > 0:
        # if heap is empty or
        # next input's left bound is smaller or equal to top heap element right bound
        # do push
        # heap only contains buildings that are "overlapped" with highest one
        if len(heap) == 0 or i < n and bs[i][0] <= heap[0][1]:
            ind = bs[i][0]
            # push all inputs with same left bound
            while i < n and bs[i][0] == ind:
                heappush(heap, (-bs[i][2], bs[i][1]))
                i += 1
        else:
            ind = heap[0][1] # top element right bound
            # pop all elements with right bound smaller or equal to "right"
            # basically discard building whose right bound is covered by top element
            # to gurantee no duplicate bound
            while len(heap) > 0 and heap[0][1] <= ind:
                heappop(heap)

        # new height is from top element or 0
        # not the element that is recently poped
        height = -heap[0][0] if len(heap) > 0 else 0
        
        # do not add duplicate height
        # no duplicate bound will be add
        # "ind" is either from "if" or "else"
        if len(skyline) == 0 or height != skyline[-1][1]:
            skyline.append([ind, height])
            
    return skyline

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
#buildings = [[1,2,1],[1,2,2]]
for pair in getSkyline(buildings):
    print pair,
print
