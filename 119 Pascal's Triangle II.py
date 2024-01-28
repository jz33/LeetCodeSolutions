'''
119. Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1]

Constraints:
    0 <= rowIndex <= 33

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prevRow = [1]
        for _ in range(rowIndex):
            row = [None] * (len(prevRow) + 1)
            row[0] = 1
            row[-1] = 1
            for i in range(1, len(row)-1):
                row[i] = prevRow[i-1] + prevRow[i]
            prevRow = row
        return prevRow