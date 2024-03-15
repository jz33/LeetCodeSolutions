'''
1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows
https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

You are given an m x n matrix mat that has its rows sorted in non-decreasing order and an integer k.
You are allowed to choose exactly one element from each row to form an array.
Return the kth smallest array sum among all possible arrays.

Example 1:

Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 7
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.

Example 2:

Input: mat = [[1,3,11],[2,4,6]], k = 9
Output: 17

Example 3:

Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
Output: 9
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.  

Constraints:
    m == mat.length
    n == mat.length[i]
    1 <= m, n <= 40
    1 <= mat[i][j] <= 5000
    1 <= k <= min(200, nm)
    mat[i] is a non-decreasing array.
''' 

class Solution:
    '''
    Based on 373. Find K Pairs with Smallest Sums
    Time Complexity: rowCount * colCount * log(k)
    '''
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        def kSmallestPairs(nums1: List[int], nums2: List[int]) -> List[int]:
            '''
            Based on 373. Find K Pairs with Smallest Sums
            For every 2 rows, get the top k sums
            '''
            heap = [] # [(sum, nums1 index, nums2 index)]
            
            def push(i1: int, i2: int):
                nonlocal heap
                if i1 < len(nums1) and i2 < len(nums2):
                    heappush(heap, (nums1[i1] + nums2[i2], i1, i2))
            
            push(0, 0)
            row = []
            while heap and len(row) < k:
                t, i1, i2 = heappop(heap)
                row.append(t)
                push(i1, i2 + 1)
                if i2 == 0:
                    push(i1 + 1, i2)
            return row 
        
        lastRow = mat[0]
        for i in range(1, len(mat)):
            lastRow = kSmallestPairs(lastRow, mat[i])
        return lastRow[k-1]
