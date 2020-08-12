/*
130.Surrounded Regions
https://leetcode.com/problems/surrounded-regions/

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.
*/
var Directions = [8]int{0, 1, 0, -1, 1, 0, -1, 0}

/*
The idea is starting from border, if 'O', apply bfs
to set all 'O' cells connected to boarder as 'V'.
Then go though matrix, update to final result.
This is different approach comparing to 1254. Number of Closed Islands.
*/
func solve(board [][]byte) {
    rowCount := len(board)
    if rowCount == 0 {
        return 
    }
    colCount := len(board[0])
    if colCount == 0 {
        return
    }
    
    bfs := func(i int, j int) {
        stack := [][]int {{i,j}}
        for len(stack) > 0 {
            var newStack [][]int
            for _, p := range stack {
                for d := 0; d < 8; d += 2 {
                    x := p[0] + Directions[d]
                    y := p[1] + Directions[d+1]
                    if x >= 0 && x < rowCount && y >= 0 && y < colCount && board[x][y] == 'O'{
                        // To avoid duplicate entry in stack,
                        // set visited here before pushing into stack
                        board[x][y] = 'V'
                        newStack = append(newStack, []int{x,y})
                    }
                }
            }
            stack = newStack
        }
    }
    
    // 1. BFS from borders
    colBorders := [2]int{0, colCount-1}
    for i := 0; i < rowCount; i++ {
        for _, j := range colBorders {
            if board[i][j] == 'O' {
                board[i][j] = 'V'
                bfs(i, j)
            }
        }
    }
    
    rowBorders := [2]int{0, rowCount-1}
    for j := 0; j < colCount; j++ {
        for _, i := range rowBorders {
            if board[i][j] == 'O' {
                board[i][j] = 'V'
                bfs(i, j)
            }
        }
    }
    
    // 2. Update result
    for i := 0; i < rowCount; i++ {
        for j := 0; j < colCount; j++ {
            if board[i][j] == 'V'{
                board[i][j] = 'O'
            } else if board[i][j] == 'O'{
                board[i][j] = 'X'
            }
        }
    }
}
