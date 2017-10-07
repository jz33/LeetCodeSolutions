public void Rotate(int[,] mat) {
    int N = mat.GetLength(0); // Not: mat.Length
    int level = (N >> 1);
    int t = 0;
    for(int i = 0;i<level;i++){
        for(int j = i;j<N-i-1;j++){
            t = mat[i,j]; // Not: mat[i][j]
            mat[i,j] = mat[N-1-j,i];
            mat[N-1-j,i] = mat[N-1-i,N-1-j];
            mat[N-1-i,N-1-j] = mat[j,N-1-i];
            mat[j,N-1-i] = t;                
        }
    }
}
