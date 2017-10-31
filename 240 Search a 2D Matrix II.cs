/*
https://leetcode.com/problems/search-a-2d-matrix-ii
This solution works both Search a 2D Matrix I & II
*/
public bool SearchMatrix(int[,] mat, int tag) {
    int row_count = mat.GetLength(0);
    int col_count = mat.GetLength(1);
    if (row_count < 1 || col_count < 1) return false;
    int r = 0;
    int c = col_count - 1;
    while(r < row_count && c > -1) {
        int e = mat[r,c];
        if (tag == e) return true;
        else if (tag < e) c -= 1;
        else r += 1;
    }
    return false;
}
