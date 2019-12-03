'''
59. Spiral Matrix II
https://leetcode.com/problems/spiral-matrix-ii/

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return [[]]
        
        res = [[None] * n for _ in range(n)]
        
        x, y = 0, 0
        level = 0 # circular layer levels
        directions = [(0,1),(1,0),(0,-1),(-1,0)] # right, down, left, up
        di = 0
        for i in range(1,  n ** 2 +1):
            res[x][y] = i
            
            if di == 0:
                if y == n - level - 1:
                    di = 1
            elif di == 1:
                if x == n - level - 1:
                    di = 2
            elif di == 2:
                if y == level:
                    di = 3
            elif di == 3:
                if x == level + 1:
                    di = 0
                    level += 1

            x += directions[di][0]
            y += directions[di][1]

        return res
