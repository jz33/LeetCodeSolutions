'''
174. Dungeon Game
https://leetcode.com/problems/dungeon-game/

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon.
The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in
the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer.
If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms;
other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows
the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)
 

Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

'''
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon or not dungeon[0]:
            return 1
        
        rowCount = len(dungeon)
        colCount = len(dungeon[0])

        # dp[i][j] is the minimum health required at (i,j)
        dp = [[0] * colCount for j in range(rowCount)]
        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])

        # Iterate backwards
        for i in range(rowCount-1, -1, -1):
            for j in range(colCount-1, -1, -1):
                h = dungeon[i][j]
                if i == rowCount-1 and j == colCount-1:
                    dp[i][j] = max(1, 1 - h)
                elif i == rowCount-1:
                    dp[i][j] = max(1, dp[i][j+1] - h)
                elif j == colCount-1:
                    dp[i][j] = max(1, dp[i+1][j] - h)
                else:
                    dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - h)
            
        return dp[0][0]
