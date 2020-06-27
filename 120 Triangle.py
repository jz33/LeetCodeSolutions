'''
120. Triangle
https://leetcode.com/problems/triangle/

Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space,
where n is the total number of rows in the triangle.
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        
        dp = [triangle[0][0]]
        for i in range(1, len(triangle)):
            row = triangle[i]
            newDp = [0] * len(row)
            
            newDp[0] = dp[0] + row[0]
            newDp[-1] = dp[-1] + row[-1]
            for j in range(1, len(row) - 1):
                newDp[j] = min(dp[j-1], dp[j]) + row[j]
                
            dp = newDp
            
        return min(dp)
