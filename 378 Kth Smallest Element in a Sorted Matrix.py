'''
378. Kth Smallest Element in a Sorted Matrix
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Given an n x n matrix where each of the rows and columns is sorted in ascending order,
return the kth smallest element in the matrix.

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

Follow up:
    Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
    Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun
'''
class Solution:
    '''
    Use heap, time: O(n * log(k)), space: O(k)
    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        size = len(matrix)
        heap = [(matrix[0][0], 0, 0)] # [(value, i, j)]
        
        count = 0
        while heap:
            value, r, c = heappop(heap)
            count += 1
            if count == k:
                return value

            if c + 1 < size:
                # Push right element
                heappush(heap, (matrix[r][c+1], r, c+1))
            if c == 0 and r + 1 < size:
                # Push down element, only need to do in 1st column
                heappush(heap, (matrix[r+1][c], r+1, c))
                
        return -1 

class Solution:
    '''
    Binary search, time O(n * log(max-min), space: O(1)
    Real Facebook interview:
    https://www.1point3acres.com/bbs/thread-1048583-1-1.html
    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        size = len(matrix)

        def binaryCount(target: int):
            '''
            Search the target in matrix.
            @return: count of elements <= target and the closest smaller or equal element to target
            '''
            count = 0
            element = matrix[0][0]
            # The staring position is opposite as in 74. Search a 2D Matrix,
            # as the question is asking kth smaller not kth largest
            row = size - 1
            col = 0
            while row > -1 and col < size:
                val = matrix[row][col]
                if val <= target:
                    element = max(element, val)
                    # All values in matrix[col][0...row] are smaller than target
                    count += row + 1
                    # Move to larger side
                    col += 1
                else:
                    row -= 1
            return count, element

        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            mid = left + (right - left) // 2
            count, element = binaryCount(mid)
            if count == k:
                return element
            elif count < k:
                # Mid cannot be the result
                left = mid + 1
            else:
                # Mid can be the result
                right = mid
        return left
