/*
1275. Find Winner on a Tic Tac Toe Game
https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places "O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where
they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.

Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"

Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: "B" wins.
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
"   "    "   "    "   "    "   "    "   "    "O  "

Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
"XXO"
"OOX"
"XOX"

Example 4:

Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
"X  "
" O "
"   "

Constraints:

1 <= moves.length <= 9
moves[i].length == 2
0 <= moves[i][j] <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.
*/
// from 348. Design Tic-Tac-Toe
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

class Solution {
    public String tictactoe(int[][] moves) {
        TicTacToe board = new TicTacToe(3);
        for (int i = 0 ; i < moves.length; ++i) {
            int[] move = moves[i];
            
            // player 1 => A, player -1 => B
            int player = (i % 2 == 0) ? 1 : -1;
            int result = board.move(move[0], move[1], player);
            if (result == player) {
                if (player == 1) {
                    return "A";
                } else if (player == -1) {
                    return "B";
                }
            }
        }
        
        return (moves.length == 9) ? "Draw" : "Pending";
    }
}
