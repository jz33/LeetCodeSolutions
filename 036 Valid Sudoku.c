#include <stdio.h>
/*
Valid Sudoku
https://oj.leetcode.com/problems/valid-sudoku/
*/
#define N 9
#define S 3
#define F 0x1FF // binary: 111111111

void insert(int* set, int i){
    *set = *set ^ (1<<i-1);
}

int isValid(int board[N][N], int set) {
    size_t i,j,x,y;
    int c;

    //valid row:
    for(i = 0;i<N;i++){
        set = 0;
        for(j = 0;j<N;j++){
			c = board[i][j];
            if(c < 1 || c > N) return 0;
            else insert(&set,c);
        }
        if(set != F) return 0;
    }
    
    //valid col:
    for(i = 0;i<N;i++){
        set = 0;
        for(j = 0;j<N;j++){
			c = board[j][i];
            if(c < 1 || c > N) return 0;
            else insert(&set,c);
        }
        if(set != F) return 0;
    }
    
    // valid square:
    for(i=0;i<S;i++){
        for(j=0;j<S;j++){
			set = 0;
            for(x =i*S;x<i*S+S;x++){
                for(y=j*S;y<j*S+S;y++){
					c = board[x][y];
                    if(c < 1 || c > N) return 0;
                    else insert(&set,c);
                }
            }
            if(set != F) return 0;
        }
    }
    return 1;
}
    
int main(int argc, char** argv){
    /*
    A set implemented by bitmap
    */
    int set = 0;
    int board[N][N] ={{3, 1, 6, 5, 7, 8, 4, 9, 2},
                      {5, 2, 9, 1, 3, 4, 7, 6, 8},
                      {4, 8, 7, 6, 2, 9, 5, 3, 1},
                      {2, 6, 3, 4, 1, 5, 9, 8, 7},
                      {9, 7, 4, 8, 6, 3, 1, 2, 5},
                      {8, 5, 1, 7, 9, 2, 6, 4, 3},
                      {1, 3, 8, 9, 4, 7, 2, 5, 6},
                      {6, 9, 2, 3, 5, 1, 8, 7, 4},
                      {7, 4, 5, 2, 8, 6, 3, 1, 9}};

    printf("isValid: %d",isValid(board,set));
	return 0;
}