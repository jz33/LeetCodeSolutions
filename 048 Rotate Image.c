#include <stdio.h>
#include <stdlib.h>
/*
Rotate Image
https://oj.leetcode.com/problems/rotate-image/
*/
int** createSpiral(int** mat, const int COL, const int ROW){
	int MAX = COL*ROW;
    /*
    "dir":
    0: upper
    1: right
    2: down
    3: left
    */
	int dir=0,x=0,y=0,ctr=1,level=0;
	
	while(ctr <= MAX){
		mat[x][y] = ctr;
        switch(dir){
        case 0:
            if(y==COL-level-1){
                dir =1;
                x++;
            } else {
                y++;
            }
            break;
        case 1:
            if(x==ROW-level-1){
                dir =2;
                y--;
            } else {
                x++;
            }
            break;
        case 2:
            if(y==level){
                dir =3;
                x--;
            } else {
                y--;
            }
            break;
        case 3:
            if(x==level+1){
                dir =0;
                level++;
                y++;
            } else {
                x--;
            }
            break;
        }
        ctr++;
    }
}
void rot90Clockwise(int** mat, const int N){
	int i,j,t;
    int lv = N>>1;
	
	for(i=0;i<lv;i++){
        for(j=i;j<N-i-1;j++){
            t = mat[i][j];
            mat[i][j] = mat[N-1-j][i];
            mat[N-1-j][i] = mat[N-1-i][N-1-j];
            mat[N-1-i][N-1-j] = mat[j][N-1-i];
            mat[j][N-1-i] = t;
        }
    }
}
int main()
{
    const int N = 6;
    int i,j;
    int** mat = (int**)malloc(sizeof(int*)*N);
    for(i=0;i<N;i++) mat[i] = (int*)malloc(sizeof(int)*N);
    
    createSpiral(mat,N,N);
    
    for(i=0;i<N;i++){
        for(j=0;j<N;j++) printf("%2d ",mat[i][j]);
        printf("\n");
    }
    printf("\n");
    
    rot90Clockwise(mat,N,N);
    for(i=0;i<N;i++){
        for(j=0;j<N;j++) printf("%2d ",mat[i][j]);
        printf("\n");
    }
    printf("\n");
    
    for(i=0;i<N;i++) free(mat[i]);
    free(mat);
    return 0;
}