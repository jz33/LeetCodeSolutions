'''
118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]

Constraints:
    1 <= numRows <= 30
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []

        result = [[1]]
        for _ in range(numRows-1):
            prevRow = result[-1]
            row = [None] * (len(prevRow) + 1)
            row[0] = 1
            row[-1] = 1
            for i in range(1, len(row)-1):
                row[i] = prevRow[i-1] + prevRow[i]
            result.append(row)

        return result
