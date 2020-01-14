'''
1240. Tiling a Rectangle with the Fewest Squares
https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

Given a rectangle of size n x m, find the minimum number of integer-sided squares that tile the rectangle.

Example 1:

Input: n = 2, m = 3
Output: 3
Explanation: 3 squares are necessary to cover the rectangle.
2 (squares of 1x1)
1 (square of 2x2)

Example 2:

Input: n = 5, m = 8
Output: 5

Example 3:

Input: n = 11, m = 13
Output: 6

Constraints:
1 <= n <= 13
1 <= m <= 13
'''
class Solution:
    def dfs(self, recHeight: int, skyline: List[int], squareCount: int):
        if squareCount >= self.minSquarecount:
            return

        # Whether rectangle is already fully filled by squares
        if all(h == recHeight for h in skyline):
            self.minSquarecount = min(self.minSquarecount, squareCount);
            return

        # Whether skyline is already computed
        key = '-'.join(str(h) for h in skyline)
        prevSolution = self.solutions.get(key, None)
        if prevSolution is not None and prevSolution <= squareCount:
            return
        self.solutions[key] = squareCount

        # Get minimun height in skyline
        minHeight, left = min((skyline[i], i) for i in range(len(skyline)))

        # minimun height position is the left most minimun height
        # Now find the right most position of minimun height
        # If putting a new square above minimum height range,
        # its size will be right - left + 1, which should be smaller than recHeight - minHeight
        right = left
        while right + 1 < len(skyline) and skyline[right+1] == minHeight and right+1 - left + 1 <= recHeight - minHeight:
            right += 1

        # Try put squre from right position first, because the new square can be maximun
        for i in range(right, left-1, -1):
            newSquareSize = i - left + 1

            nextSkyline = copy.deepcopy(skyline)
            for k in range(left, i+1):
                nextSkyline[k] += newSquareSize
            
            self.dfs(recHeight, nextSkyline, squareCount + 1)
        
    def tilingRectangle(self, n: int, m: int) -> int:
        if n == m:
            return 1

        if n > m: # let n be smaller
            n, m = m, n

        self.minSquarecount = float('inf')
        self.solutions = {} # {skyline hash : square count}

        # skyline along n side is records height on each position
        # e.g., if skyline = [0,2,2], it means there is a sqaure of size 2
        skyline = [0] * n
        self.dfs(m, skyline, 0)
        return self.minSquarecount
