#include <stdio.h>
/*
Sudoku Solver
https://oj.leetcode.com/problems/sudoku-solver/
http://www.geeksforgeeks.org/backtracking-set-7-suduku/
A backtrackign approach
*/
#define N 9
#define S 3
/* A utility function to print grid  */
void printGrid(int grid[N][N])
{
    int row,col;
    for(row = 0; row < N; row++){
        for(col = 0; col < N; col++)
            printf("%2d", grid[row][col]);
        printf("\n");
    }
}
/* Returns a boolean which indicates whether any assigned entry
   in the specified row matches the given number. */
int UsedInRow(int grid[N][N], int row, int num)
{
    int col;
    for(col = 0; col < N; col++)
        if(grid[row][col] == num) return 1;
    return 0;
}
/* Returns a boolean which indicates whether any assigned entry
   in the specified column matches the given number. */
int UsedInCol(int grid[N][N], int col, int num)
{
    int row;
    for(row = 0; row < N; row++)
        if (grid[row][col] == num) return 1;
    return 0;
}
/* Returns a boolean which indicates whether any assigned entry
   within the specified 3x3 box matches the given number. */
int UsedInBox(int grid[N][N], int boxStartRow, int boxStartCol, int num)
{
    int row,col;
    for(row = 0; row < S; row++)
        for(col = 0; col < S; col++)
            if (grid[row+boxStartRow][col+boxStartCol] == num)
                return 1;
    return 0;
}
/* Returns a boolean which indicates whether it will be legal to assign
   num to the given row,col location. */
int isSafe(int grid[N][N], int row, int col, int num)
{
    /* Check if 'num' is not already placed in current row,
       current column and current 3x3 box */
    return !UsedInRow(grid, row, num) &
           !UsedInCol(grid, col, num) &
           !UsedInBox(grid, row - row%3 , col - col%3, num);
}

/* Searches the grid to find an entry that is still unassigned. If
   found, the reference parameters row, col will be set the location
   that is unassigned, and true is returned. If no unassigned entries
   remain, false is returned. */
int FindUnassignedLocation(int grid[N][N], int* row, int* col)
{
    int r,c;
    *row = -1;
    *col = -1;
    for (r = 0; r < N; r++)
        for (c = 0; c < N; c++)
            if (grid[r][c] == 0){
                *row = r;
                *col = c;
                return 1;
            }
    return 0;
}
/* Takes a partially filled-in grid and attempts to assign values to
  all unassigned locations in such a way to meet the requirements
  for Sudoku solution (non-duplication across rows, columns, and boxes) */
int SolveSudoku(int grid[N][N])
{
    int row, col, num;
 
    // If there is no unassigned location, we are done
    if (!FindUnassignedLocation(grid, &row, &col))
       return 1; // success!
 
    // consider digits 1 to 9
    for (num = 1; num <= N; num++)
    {
        // if looks promising
        if (isSafe(grid, row, col, num))
        {
            // make tentative assignment
            grid[row][col] = num;
 
            // return, if success, yay!
            if(SolveSudoku(grid)) return 1;
 
            // failure, unmake & try again
            grid[row][col] = 0;
        }
    }
    return 0;
}
/*
Tester
*/
int main(){
    int grid[N][N] = {{3, 0, 6, 5, 0, 8, 4, 0, 0},
                      {5, 2, 0, 0, 0, 0, 0, 0, 0},
                      {0, 8, 7, 0, 0, 0, 0, 3, 1},
                      {0, 0, 3, 0, 1, 0, 0, 8, 0},
                      {9, 0, 0, 8, 6, 3, 0, 0, 5},
                      {0, 5, 0, 0, 9, 0, 6, 0, 0},
                      {1, 3, 0, 0, 0, 0, 2, 5, 0},
                      {0, 0, 0, 0, 0, 0, 0, 7, 4},
                      {0, 0, 5, 2, 0, 6, 3, 0, 0}};
    
    if(SolveSudoku(grid) == 1) printGrid(grid);
    else printf("No solution exists");
    return 0;
}