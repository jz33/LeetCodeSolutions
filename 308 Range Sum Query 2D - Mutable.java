/*
Range Sum Query 2D - Mutable
https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/
*/
public class NumMatrix {

    int data[][];
    int tree[][];
    int R;
    int C;

    public NumMatrix(int[][] matrix) {
        R = matrix.length;
        if(R == 0) return;
        C = matrix[0].length;
        if(C == 0) return;
        data = new int[R][C];
        // Notice the reason to use extra row and col
        tree = new int[R+1][C+1]; 
        for(int i = 0;i<R;i++)
            for(int j = 0;j<C;j++)
                update(i,j,matrix[i][j]);
    }

    public void update(int row, int col, int val) {
        if(data == null) return;
        int diff = val - data[row][col];
        data[row][col] = val;
        for(int i = row+1;i<=R;i += (i & -i))
            for(int j = col+1;j<=C;j += (j & -j))
                tree[i][j] += diff;
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        if(data == null) return 0;
        return sum(row2 + 1, col2 + 1) - sum(row2 + 1, col1) - sum(row1, col2 + 1) + sum(row1, col1);
    }
    
    private int sum(int row, int col){
        int r = 0;
        // Not i >= 0
        for(int i = row;i > 0;i -= (i & -i))
            for(int j = col;j > 0;j -= (j & -j))
                r += tree[i][j];
        return r;
    }
}
