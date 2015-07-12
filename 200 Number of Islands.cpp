#include<iostream>
#include<sstream>
#include<vector>
#include<utility>
/*
Number of Islands
https://leetcode.com/problems/number-of-islands/

Naive DFS, O(N^2)
*/
typedef std::vector<char> VEC;
typedef std::vector<VEC> MAT;
typedef std::pair<size_t,size_t> PAIR;

#define MAKE std::make_pair
#define WATER '0'
#define LAND '1'
#define VISITED '2'

void dumpVec(VEC& in){
    for(auto i = in.begin();i!=in.end();i++)
        std::cout<<*i<<" ";
    printf("\n");
}

void dumpMat(MAT& in){
    for(auto i = in.begin();i!=in.end();i++)
        dumpVec(*i);
    printf("\n");
}

/*
Find next unvisited land point starting from $ori.
*/
bool nextUnvisitedLand(MAT& grid, PAIR& ori)
{
    size_t i,j;
    
    i = ori.first;
    for(j = ori.second;j < grid[i].size();j++)
    {
        if(grid[i][j] == LAND)
        {
            ori.first = i;
            ori.second = j;
            return true;
        } 
    }
    
    for(i = ori.first + 1;i<grid.size();i++)
    {
        for(j = 0;j<grid[i].size();j++) 
        {
            if(grid[i][j] == LAND)
            {
                ori.first = i;
                ori.second = j;
                return true;
            }
        }
    }
    return false;
}
/*
Mark all adjacent land points recursively.
Initial input point must be valid.
*/
void mark(MAT& grid, PAIR ori)
{
    size_t i = ori.first;
    size_t j = ori.second;
    
    if(grid[i][j] == LAND)
    {
        grid[i][j] = VISITED;
        if(i>0) mark(grid,MAKE(i-1,j));
        if(i<grid.size()-1) mark(grid,MAKE(i+1,j));
        if(j>0) mark(grid,MAKE(i,j-1));
        if(j<grid[i].size()-1) mark(grid,MAKE(i,j+1));
    }
}

int numIslands(MAT& grid)
{
    size_t i,j;
    if(grid.size() == 0) return 0;
    
    PAIR ori = MAKE(0,0);
    int ret = 0;
    
    while(nextUnvisitedLand(grid,ori))
    {
        ret += 1;
        mark(grid,ori);
    }
    
    //dumpMat(grid);
    return ret;
}

int main()
{
    size_t i,j;
    /*
    std::string input[] = {\
        "11110",\
        "11010",\
        "11000",\
        "00000" \
    };
    */
    
    std::string input[] = {\
        "11000",\
        "11000",\
        "00100",\
        "00011" \
    };
    
    MAT mat;
    for(i=0;i<sizeof(input)/sizeof(std::string);i++)
    {
        VEC row(input[i].size(),'0');
        for(j=0;j<input[i].size();j++)
        {
            row[j] = input[i][j];
        }
        mat.push_back(row);
    }
    
    dumpMat(mat);
    std::cout<<numIslands(mat)<<"\n";
    
    return 0;
}
