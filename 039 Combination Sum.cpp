#include <iostream>
#include <vector>
#include <algorithm>
/*
Combination Sum
https://leetcode.com/problems/combination-sum/

Classic backtracking

There are 3 type of questions, for example, give [1,2,3], and target = 4
If only allowing use each number once, result is:
    (1,3)
And CL will be:
    recursive(input,sofar,i+1,tag - input[i]);
If allowing use each number infinite times, result is:
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 3)
    (2, 2)
And CL will be:
    recursive(input,sofar,i,tag - input[i]);
If allowing use each number infinite times, and different result order is count as differen result:
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 3)
    (2, 1, 1)
    (2, 2)
    (3, 1)
And CL will be:
    recursive(input,sofar,0,tag - input[i]);
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
                recursive(input,sofar,i,tag - input[i]); // Critial Line (CL)
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
