/*
348. Design Tic-Tac-Toe
https://leetcode.com/problems/design-tic-tac-toe/

Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n2) per move() operation?
*/
class TicTacToe {
    
    // The size is width * 2 +  2, row count + column count + 2 diagonals
    // counter[i] records the filled blocks diff between 2 players
    private int[] counter;
    private int width;
    
    /** Initialize your data structure here. */
    public TicTacToe(int n) {
        width = n;        
        counter = new int[n * 2 + 2];
    }
    
    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    public int move(int row, int col, int player) {
        int block = (player == 1 ? 1 : -1);
        
        // Is current row filled ?
        if (updateAndJudge(row, block)) {
            return player;
        }
        
        // Is current column filled ?
        if (updateAndJudge(col + width, block)) {
            return player;
        }
        
        // Is top-left to bottom-right diagonal filled ?
        if (row == col && updateAndJudge(width * 2, block)) {
            return player;
        }
        
        // Is top-right to bottom-left diagonal filled ?
        if (row == width - 1 - col && updateAndJudge(width * 2 + 1, block)) {
            return player;
        }

        return 0;
    }
    
    /**
        @param row index of a row, a column or one of the 2 diag
        @param block 1 or -1
        @return true if there is a win or false if there is not yet a win
    */
    private boolean updateAndJudge(int index, int block) {
        counter[index] += block;
        return Math.abs(counter[index]) == width;
    }
}

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n);
 * int param_1 = obj.move(row,col,player);
 */
