/*
1275. Find Winner on a Tic Tac Toe Game
https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

    Players take turns placing characters into empty squares ' '.
    The first player A always places 'X' characters, while the second player B always places 'O' characters.
    'X' and 'O' characters are always placed into empty squares, never on filled ones.
    The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
    The game also ends if all squares are non-empty.
    No more moves can be played if the game is over.

Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli].
return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw".
If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.

Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.

Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.

Constraints:
    1 <= moves.length <= 9
    moves[i].length == 2
    0 <= rowi, coli <= 2
    There are no repeated elements on moves.
    moves follow the rules of tic tac toe.
*/
// From 348. Design Tic-Tac-Toe
class TicTacToe {
    private width: number;
    // Save the record of the filling on each row.
    // If rowFill[i] = width or -width, a winner.
    private rowFills: number[];
    private columnFills: number[];
    private diagonalFills: number[];

    constructor(n: number) {
        this.width = n;
        this.rowFills = new Array(n).fill(0);
        this.columnFills = new Array(n).fill(0);
        this.diagonalFills = [0, 0];
    }

    move(row: number, col: number, player: 'A' | 'B'): 'A' | 'B' | 'Pending' {
        const block = player == 'A' ? 1 : -1;
        // Row
        this.rowFills[row] += block;
        if (Math.abs(this.rowFills[row]) === this.width) {
            return player;
        }
        // Column
        this.columnFills[col] += block;
        if (Math.abs(this.columnFills[col]) === this.width) {
            return player;
        }
        // Top-left to bottom-right diagonal
        if (row === col) {
            this.diagonalFills[0] += block;
            if (Math.abs(this.diagonalFills[0]) === this.width) {
                return player;
            }
        }
        // Top-right to bottom-left diagonal
        if (row === this.width - 1 - col) {
            this.diagonalFills[1] += block;
            if (Math.abs(this.diagonalFills[1]) === this.width) {
                return player;
            }
        }
        return 'Pending';
    }
}

function tictactoe(moves: number[][]): string {
    const board = new TicTacToe(3);
    for (let i = 0; i < moves.length; i++) {
        const player = (i % 2 === 0) ? 'A' : 'B';
        const result = board.move(moves[i][0], moves[i][1], player);
        if (['A', 'B'].includes(result)) {
            return result;
        }
    }
    return moves.length === 9 ? 'Draw' : 'Pending';
};
