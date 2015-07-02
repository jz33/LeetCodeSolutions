#include <iostream>
#include <sstream>
#include <vector>
/*
N-Queens
https://leetcode.com/problems/n-queens/
*/
typedef std::vector<std::string> MAT;
typedef std::vector<int> VEC;

std::vector<MAT> pool;

int intabs(int a)
{
    return a > 0 ? a : -a;
}

void solve(int n, VEC& buf, int col_index)
{
    int i,j,safe;
    for(i = 0;i < n;i++) // iterative by rows
    {
        buf[col_index] = i;
        
        safe = 1;
        for(j = 0;j < col_index;j++) // iterative by cols
        {
            // same row || same diagonal
            if(buf[j] == i || intabs(j - col_index) == intabs(buf[j] - i))
            {
                safe = 0;
                break;
            }
        }

        if(safe)
        {
            if(col_index == n - 1)
            {
                MAT solution(n, std::string(n, '.'));
                for(j = 0;j < n;j++) solution[buf[j]][j] = 'Q';
                pool.push_back(solution);
            }
            else
                solve(n, buf, col_index + 1);
        }
    }
}

std::vector<MAT> solveNQueens(int n)
{
    int col_index = 0;
    /*
    $buf use a vector to record current solution
    i => buf[i] : col => row
    */
    VEC buf(n, -1);
    
    pool.clear();
    solve(n,buf, col_index);
    return pool;
}

void dump(void)
{
    size_t i,j;
    for(i = 0;i!=pool.size();i++)
    {
        for(j=0;j!=pool[i].size();j++)
        {
            std::cout<<pool[i][j]<<"\n";
        }
        printf("\n");
    }
}

int main()
{
    int n = 4;
    solveNQueens(n);
    dump();
    return 0;
}
