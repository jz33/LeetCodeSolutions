#include<iostream>
#include<sstream>
#include<vector>
#include<utility>
/*
Surrounded Regions
https://leetcode.com/problems/surrounded-regions/
Similar to "200 Number of Islands"
*/
typedef std::vector<char> VEC;
typedef std::vector<VEC> MAT;
typedef std::pair<size_t,size_t> PAIR;

#define MAKE std::make_pair
#define WATER 'X'
#define LAND 'O'
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
void mark(MAT& grid, PAIR ori, bool& island)
{
    size_t i = ori.first;
    size_t j = ori.second;
    
    if(grid[i][j] == LAND)
    {
        grid[i][j] = VISITED;
        
        if(i == 0 || i == grid.size() - 1 
        || j == 0 || j == grid[i].size() - 1)
        {
            island = false;
        }
        else
        {
            mark(grid,MAKE(i-1,j),island);
            mark(grid,MAKE(i+1,j),island);
            mark(grid,MAKE(i,j-1),island);
            mark(grid,MAKE(i,j+1),island);
        }
        if(island)
            grid[i][j] = WATER;
    }
}

void numIslands(MAT& grid)
{
    size_t i,j;
    if(grid.size() == 0 || grid[0].size() == 0) return;
    
    PAIR ori = MAKE(0,0);
    int ret = 0;
    
    while(nextUnvisitedLand(grid,ori))
    {
        ret += 1;
        bool island = true;
        mark(grid,ori,island);
    }
    
    dumpMat(grid);
    
    for(i = 0;i<grid.size();i++)
        for(j = 0;j<grid[i].size();j++)
            if(grid[i][j] == VISITED)
                grid[i][j] = LAND;
                
    dumpMat(grid);
}

int main()
{
    size_t i,j;
    
    // std::string input[] = {\
//         "XXXX",\
//         "XOOX",\
//         "XOOX",\
//         "XOXX" \
//     };

    std::string input[] = {"OOOOOOO"};
    
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
    numIslands(mat);
    
    return 0;
}
