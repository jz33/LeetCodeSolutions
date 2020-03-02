'''
840. Magic Squares In Grid
https://leetcode.com/problems/magic-squares-in-grid/

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column,
and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
        
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
'''
class Solution:               
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(rowStart, colStart) -> bool:
            if grid[rowStart+1][colStart+1] != 5:
                # Center must be 5
                return False

            bitmap = 1 # bitmap to check duplication
            rs = [0, 0, 0] # sum of rows
            cs = [0, 0, 0] # sum of columns
            for i in range(rowStart, rowStart + 3):
                for j in range(colStart, colStart + 3):
                    e = grid[i][j]
                    bitmap = bitmap ^ (1 << e)
                    if (bitmap & (1 << e)) == 0:
                        # duplicate number
                        return False
                    rs[i-rowStart] += e
                    cs[j-colStart] += e      

            return bitmap == 0x3FF and all(s == 15 for s in rs) and all (s == 15 for s in cs)

        return sum(isMagic(i, j) for i in range(len(grid)-2) for j in range(len(grid[0])-2))
