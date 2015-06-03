#include <iostream>
#include <sstream>
#include <vector>
/*
079 Word Search
https://leetcode.com/problems/word-search/
*/
#define DEBUG 1
#define VISITED '#'

typedef std::vector<std::string> Matrix;

size_t ROW = 0;
size_t COL = 0;
/*
079
DFS + backtracking
O(ROW * COL * 3 ^ Strlen)
*/
int exist(Matrix mat, const char* tag, int row, int col)
{
    char ori;
    if (*tag == '\0')
        return 1;
    if(mat[row][col] != *tag || mat[row][col] == VISITED)
        return 0; 
    
    ori = mat[row][col];
    mat[row][col] = VISITED;
    
    if ((row > 0 && exist(mat,tag+1, row - 1, col)) ||
        (row < ROW - 1 && exist(mat,tag+1, row + 1, col)) ||
        (col > 0 && exist(mat,tag+1, row, col - 1)) ||
        (col < COL - 1 && exist(mat,tag+1, row, col + 1))) {
        mat[row][col] = ori;
        return true;
    }
    else
    {
        mat[row][col] = ori;
        return false;
    }
}

int wordSeach(Matrix mat,const char* tag)
{
    int i,j;
    for(i = 0;i<ROW;i++)
        for(j = 0;j<COL;j++)
            if (exist(mat,tag,i,j))
                return 1;
    return 0;
}

void test(void)
{
    int i;
    char* strs[] = {
        "ABCE",
        "SFCS",
        "ADEE"
    };

    char* arr[] = {
        "ABCCED",
        "SEE",
        "ABCB"
    };

    Matrix mat;
    for(i = 0;i<sizeof(strs)/sizeof(char*);i++)
    {
        mat.push_back(std::string(strs[i]));      
    }
    ROW = mat.size();
    COL = mat[0].size();
    
    for(i = 0;i<sizeof(arr)/sizeof(char*);i++)
        printf("%d\n",wordSeach(mat,arr[i]));
}
int main()
{
    test();
    return 0;
}
