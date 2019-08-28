#include <iostream>
#include <vector>
#include <algorithm>
/*
Combination Sum II
https://leetcode.com/problems/combination-sum-ii/

Classic backtracking
*/
std::vector<std::vector<int> > pool;

void recursive(std::vector<int>& input, std::vector<int>& sofar, int start, int tag)
{
    if(tag == 0)
    {
        pool.push_back(sofar);
    }
    else if(tag > 0)
    {
        for(int i = start;i<input.size();i++)
        {
            if(i>start && input[i] == input[i-1]) 
                continue;
            if(input[i] <= tag)
            {
                sofar.push_back(input[i]);
                recursive(input,sofar,i+1,tag - input[i]); // here uses i+1, while Question 39 uses i
                sofar.pop_back();
            }
        }
    }
}
std::vector<std::vector<int> > combinationSum(std::vector<int>& input, int tag)
{
    pool.clear();
    
    std::stable_sort(input.begin(),input.end());
    std::vector<int> sofar;
    recursive(input,sofar,0,tag);
    
    return pool;
}
int main()
{   
    return 0;
}
