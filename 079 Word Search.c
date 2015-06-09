#include <stdio.h>
#include <stdlib.h>
/*
079 Word Search
https://leetcode.com/problems/word-search/
*/
#define VISITED '#'

int ROW = 0;
int COL = 0;
/*
079
DFS + backtracking
O(ROW * COL * 3 ^ Strlen)
*/
int wordSearchRec(char** mat, const char* tag, int row, int col)
{
    char ori;
    if(mat[row][col] != *tag || mat[row][col] == VISITED)
        return 0; 
    if(*(tag+1) == '\0')
        return 1;

    ori = mat[row][col];
    mat[row][col] = VISITED;
    
    if ((row > 0 && wordSearchRec(mat,tag+1, row - 1, col)) ||
        (row < ROW - 1 && wordSearchRec(mat,tag+1, row + 1, col)) ||
        (col > 0 && wordSearchRec(mat,tag+1, row, col - 1)) ||
        (col < COL - 1 && wordSearchRec(mat,tag+1, row, col + 1))) {
        mat[row][col] = ori;
        return true;
    }
    else
    {
        mat[row][col] = ori;
        return false;
    }
}

int wordSeach(char** mat,char* tag)
{
    int i,j;
    for(i = 0;i<ROW;i++)
        for(j = 0;j<COL;j++)
            if (wordSearchRec(mat,tag,i,j))
                return 1;
    return 0;
}

// api
int exist(char** board, int boardRowSize, int boardColSize, char* word)
{
    ROW = boardRowSize;
    COL = boardColSize;
    return wordSeach(board,word) == 1;
}

void test(void)
{
    char** mat;
    char* word = "a";
    int i;
    
    ROW = 1;
    COL = 1;
    
    mat = (char**)malloc(sizeof(char*)*ROW);
    for(i=0;i<ROW;i++)
        mat[i] = (char*)malloc(sizeof(char)*COL);
    
    mat[0][0] = 'a';
    printf("%d\n",exist(mat,ROW,COL,word));
    
    for(i=0;i<ROW;i++)
        free(mat[i]);
    free(mat);
}

int main()
{
    test();
    return 0;
}
