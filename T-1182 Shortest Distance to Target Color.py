'''
1182. Shortest Distance to Target Color
https://leetcode.com/problems/shortest-distance-to-target-color/

You are given an array colors, in which there are three colors: 1, 2 and 3.

You are also given some queries. Each query consists of two integers i and c,
return the shortest distance between the given index i and the target color c.
If there is no solution return -1.

 

Example 1:

Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]
Explanation: 
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).

Example 2:

Input: colors = [1,2], queries = [[0,3]]
Output: [-1]
Explanation: There is no 3 in the array.
 

Constraints:

1 <= colors.length <= 5*10^4
1 <= colors[i] <= 3
1 <= queries.length <= 5*10^4
queries[i].length == 2
0 <= queries[i][0] < colors.length
1 <= queries[i][1] <= 3
'''
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        INF = float('inf')
        size = len(colors)
        
        # dp[i] is a 3 sized array stores a pair of closest index with that color
        # dp[i][j = [closet index, closest distance], j in range(3)
        dp = [None] * size      
        
        # left to right
        for i in range(size):
            color = colors[i] - 1
            dp[i] = [[-1, INF], [-1, INF], [-1, INF]]
            for j in range(3):
                if j == color:
                    dp[i][j] = [i,0]
                elif i > 0:
                    dp[i][j] = [dp[i-1][j][0], dp[i-1][j][1] + 1 if dp[i-1][j][0] != -1 else INF]
        
        # right to left
        for i in range(size-1,-1,-1):       
            color = colors[i] - 1
            for j in range(3):
                if j == color:
                    dp[i][j] = [i,0]
                elif i < size - 1:
                    if dp[i+1][j][0] != -1 and dp[i+1][j][1] + 1 < dp[i][j][1]:
                        dp[i][j] = [dp[i+1][j][0], dp[i+1][j][1] + 1]
        
        return [dp[index][color-1][1] if dp[index][color-1][0] != -1 else -1 for index, color in queries] 
