public class TicTacToe {

    int[] ctr;
    int n;

    /** Initialize your data structure here. */
    public TicTacToe(int n) {
        this.n = n;
        ctr = new int[n*2+2];// row count + colunm count + 2 diagonals
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
        int c = 1;
        if(player == 2) c = -1;
        
        int index = row;
        ctr[index] += c;
        if(Math.abs(ctr[index]) == n) return player;
        
        index = n + col;
        ctr[index] += c;
        if(Math.abs(ctr[index]) == n) return player;
        
        if(row == col){
            index = n * 2;
            ctr[index] += c;
            if(Math.abs(ctr[index]) == n) return player;
        }
        if(row + col == n - 1){
            index = n * 2 + 1;
            ctr[index] += c;
            if(Math.abs(ctr[index]) == n) return player;
        }
        return 0;
    }
}
