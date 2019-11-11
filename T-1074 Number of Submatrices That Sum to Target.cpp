/*
1074. Number of Submatrices That Sum to Target
https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

Given a matrix, and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: 
for example, if x1 != x1'.

Example 1:

Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
*/
class Solution
{
public:
    // This part is using 560 Subarray Sum Equals K
    int countOfSubarrayEqualsTarget(std::vector<int>& arr, int target)
    {
        std::unordered_map<int, int> accuSet; // accumalations : count
        accuSet.emplace(0, 1);
        
        int acc = 0;
        int res = 0;       
        for (int e : arr)
        {
            acc += e;
            
            auto it = accuSet.find(acc - target);
            if (it != accuSet.end())
            {
                res += it->second;
            }
            
            auto tt = accuSet.find(acc);
            if (tt != accuSet.end())
            {
                accuSet[acc] = tt->second + 1;
            }
            else
            {
                accuSet[acc] = 1; 
            }                 
        }
        return res;
    }
    
    // This part is using 363 Max Sum of Rectangle No Larger Than K
    int numSubmatrixSumTarget(std::vector<std::vector<int>>& matrix, int target)
    {   
        if (matrix.empty())
        {
            return target == 0 ? 1 : 0;
        }
        
        int rowCount = matrix.size();
        int colCount = matrix[0].size();
        int totalSum = 0;
        
        // Iterate to get all possible accumulation "on a row", i.e., 
        // @accs records all submatrix sums
        // The outer loop should iterate rowCount or colCount who is smaller       
        if (rowCount <= colCount)
        {
            for (int r = 0; r < rowCount; ++r)
            {
                std::vector<int> accs(colCount, 0);
                for (int i = r; i < rowCount; ++i)
                {
                    for (int j = 0; j < colCount; ++j)
                    {
                        accs[j] += matrix[i][j];
                    }
                    
                    totalSum += countOfSubarrayEqualsTarget(accs, target);
                }            
            }
        }
        else
        {
            for (int c = 0; c < colCount; ++c)
            {
                std::vector<int> accs(rowCount, 0);
                for (int j = c; j < colCount; ++j)
                {
                    for (int i = 0; i < rowCount; ++i)
                    {
                        accs[i] += matrix[i][j];
                    }                
                    totalSum += countOfSubarrayEqualsTarget(accs, target);
                }            
            }
        }
        return totalSum;
    }
};
