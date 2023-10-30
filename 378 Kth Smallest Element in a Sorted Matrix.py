'''
378. Kth Smallest Element in a Sorted Matrix
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:

Input: matrix = [[-5]], k = 1
Output: -5

Constraints:

    n == matrix.length == matrix[i].length
    1 <= n <= 300
    -109 <= matrix[i][j] <= 109
    All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
    1 <= k <= n2
'''
from heapq import heappush, heappop

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        size = len(matrix)
        heap = [] # min heap, (value, i, j), compares value
        
        def push(i,j):
            nonlocal heap
            if i < size and j < size:
                heappush(heap, (matrix[i][j], i, j))
                
        push(0,0)
        count = 0
        while heap:
            value, i, j = heappop(heap)
            count += 1
            if count == k:
                return value

            push(i, j + 1)
            # Only need to go right on first row,
            # as later rows are pushed from top.
            if j == 0:
                push(i + 1, j)
                
        return -1 
