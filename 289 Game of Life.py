'''
Game of Life
https://leetcode.com/problems/game-of-life/
'''
def getLiveCount(board,i,j):
    count = 0
    if i + 1 < len(board):
        e = board[i+1][j]
        if ( e & 1 ) == 1: count += 1
        if j + 1 < len(board[i]):
            e = board[i+1][j+1]
            if ( e & 1 ) == 1: count += 1
        if j - 1 > - 1:
            e = board[i+1][j-1]
            if ( e & 1 ) == 1: count += 1
    if i - 1 > - 1:
        e = board[i-1][j]
        if ( e & 1 ) == 1: count += 1
        if j + 1 < len(board[i]):
            e = board[i-1][j+1]
            if ( e & 1 ) == 1: count += 1
        if j - 1 > - 1:
            e = board[i-1][j-1]
            if ( e & 1 ) == 1: count += 1
    
    if j + 1 < len(board[i]):        
        e = board[i][j+1]
        if ( e & 1 ) == 1: count += 1            
    if j - 1 > -1:       
        e = board[i][j-1]
        if ( e & 1 ) == 1: count += 1
        
    return count

'''
0 : dead
1 : live
2 : live, was dead
3 : dead, was live
'''
def gameOfLife(board):
    for i in xrange(len(board)):
        for j in xrange(len(board[i])):
            n = getLiveCount(board,i,j)
            print i,j,n
            if board[i][j] > 0: 
                if n < 2 or n > 3:
                    board[i][j] = 3
            else:
                if n == 3:
                    board[i][j] = 2
    
    for i in xrange(len(board)):
        for j in xrange(len(board[i])):
            e = board[i][j]
            board[i][j] = ((e >> 1) ^ (e & 1))
