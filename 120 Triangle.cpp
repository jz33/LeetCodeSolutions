#include <iostream>
#include <vector>
#include <algorithm>
/*
120 Triangle
https://oj.leetcode.com/problems/triangle/
*/
typedef std::vector<int> VEC;
typedef std::vector<VEC> MAT;

class Solution {
public:
    int minimumTotal(MAT& mat)
    {
        if(mat.size() < 1) return 0;
        VEC& prev = mat[0];
        
        for(size_t j = 1;j < mat.size();j++)
        {
            VEC& curr = mat[j];
            
            curr[0] += prev[0];
            for(std::size_t i = 0;i < j - 1;i++)
            {
            	curr[i+1] += std::min(prev[i],prev[i+1]);
            }
            curr[j] += prev[j-1];
            prev = curr;
        }
        return *std::min_element(prev.begin(),prev.end());
    }
};
