'''
Dungeon Game
https://leetcode.com/problems/dungeon-game/
'''
def calculateMinimumHP(dungeon):
    """
    :type dungeon: List[List[int]]
    :rtype: int
    """
    R = len(dungeon)
    if R == 0: return 1
    C = len(dungeon[0])
    
    health = [[0 for i in xrange(0,C)] for j in xrange(0,R)] # R*C
    
    health[R-1][C-1] = max(1,1 - dungeon[R-1][C-1]) # seed

    for i in xrange(R-2,-1,-1):   
        health[i][C-1] = max(1,health[i+1][C-1] - dungeon[i][C-1])
    
    for j in xrange(C-2,-1,-1):   
        health[R-1][j] = max(1,health[R-1][j+1] - dungeon[R-1][j])
        
    for i in xrange(R-2,-1,-1):
        for j in xrange(C-2,-1,-1):
            health[i][j] = max(1,min(health[i][j+1],health[i+1][j]) - dungeon[i][j])

    return health[0][0]
