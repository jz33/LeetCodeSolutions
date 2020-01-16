from typing import List, Tuple
from heapq import heappush, heappop
'''
https://leetcode.com/discuss/interview-question/476340/Google-or-Onsite-or-Min-Modifications

Given a matrix of direction with L, R, U, D, at any point you can move to the direction which is written over the cell [i, j].
We have to tell minimum number of modifications to reach from [0, 0] to [N - 1, M - 1] .

Example :-
R R D
L L L
U U R
Answer is 1, we can modify cell [1, 2] from L To D.

PS: I was not able to solve it during the interview, but in the end of the interview I got a nice idea
to solve the problem but interviewer was not interested in listening as time was up and I was not 100% sure
about that so I did not insist but later I found that was the correct solution.

I want to see how other people solve this problem, I will reveal the answer later, with time complexity of O(N * M)
'''
class Solution:
    def nextMove(self, i: int, j: int, direction: str) -> Tuple[int, int]:
        if direction == 'R':
            return i, j+1
        if direction == 'D':
            return i+1, j
        if direction == 'L':
            return i, j-1
        if direction == 'U':
            return i-1, j

    def minModification(self, mat: List[str]) -> int:
        rowCount = len(mat)
        colCount = len(mat[0])
        maxVal = rowCount * colCount

        # Global visited check, {(i,j) : modification count}
        visited = [[maxVal] * colCount for _ in range(rowCount)]
        visited[0][0] = 0

        heap = [(0,0,0)] # [(modification count, x, y)]
        while heap:
            mc, i, j = heappop(heap)
            oldDir = mat[i][j]
            for newDir in ['R', 'D', 'L', 'U']:
                x,y = self.nextMove(i,j,newDir)
                newMc = mc if oldDir == newDir else mc + 1
                if 0 <= x < rowCount and 0 <= y < colCount and newMc < visited[x][y]:
                    if x == rowCount - 1 and y == colCount - 1:
                        return newMc

                    visited[x][y] = newMc
                    heappush(heap, (newMc, x, y))

        return -1

sol = Solution()

matrix = [
'RRD',
'LLL',
'UUR',
]

matrix = [
'RRR',
'LLL',
'RRR',
'LLL',
'LLL',
]

print(sol.minModification(matrix))
