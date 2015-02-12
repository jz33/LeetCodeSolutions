#include <stdio.h>
#include <stdlib.h>
/*
54 Spiral Matrix
https://oj.leetcode.com/problems/spiral-matrix/
59 Spiral Matrix II
https://oj.leetcode.com/problems/spiral-matrix-ii/
*/
// 59
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
// 54
void printSpiral(int** mat, const int COL, const int ROW){
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
		printf("%d ",mat[x][y]);
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
int main()
{
    const int N = 5;
    int i,j;
    int** mat = (int**)malloc(sizeof(int*)*N);
    for(i=0;i<N;i++) mat[i] = (int*)malloc(sizeof(int)*N);
    
    createSpiral(mat,N,N);
    
    for(i=0;i<N;i++){
        for(j=0;j<N;j++) printf("%d ",mat[i][j]);
        printf("\n");
    }
    printf("\n");
    
    printSpiral(mat,N,N);
    printf("\n");
    
    for(i=0;i<N;i++) free(mat[i]);
    free(mat);
    return 0;
}