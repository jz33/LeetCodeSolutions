'''
378. Kth Smallest Element in a Sorted Matrix
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Given a n x n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

Note:

You may assume k is always valid, 1 ≤ k ≤ n2.
'''
from heapq import heappush, heappop

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        
        def push(i,j):
            nonlocal heap
            if i < n and j < n:
                heappush(heap, (matrix[i][j], i, j))
                
        push(0,0)
        ctr = 0
        while heap and ctr < k:
            r, i, j = heappop(heap)
            ctr += 1
            if ctr == k:
                return r
            
            push(i, j + 1)
            if j == 0:
                push(i + 1, j)
                
        return -1        
