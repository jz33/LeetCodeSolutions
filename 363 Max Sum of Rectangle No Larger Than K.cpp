/*
363. Max Sum of Rectangle No Larger Than K
https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:

Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2

Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).
             
Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
*/
class Solution {
public:
    int maxSubArraySumNoLargerThanK(std::vector<int>& arr, int k)
    {
        std::set<int> accuSet;
        accuSet.insert(0);
        
        int acc = 0;
        int maxVal = INT_MIN;       
        for (int e : arr)
        {
            acc += e;
            auto it = accuSet.lower_bound(acc - k);
            if (it != accuSet.end())
            {
                maxVal = std::max(maxVal, acc - *it);                
            }
            accuSet.insert(acc);
        }
        return maxVal;
    }
        
    int maxSumSubmatrix(std::vector<std::vector<int>>& matrix, int k)
    {   
        if (matrix.empty())
        {
            return 0;
        }
        
        int rowCount = matrix.size();
        int colCount = matrix[0].size();
        int maxSum = INT_MIN;
        
        // Iterate to get all possible accumulation "on a row", i.e., 
        // @accs records all submatrix sums.
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
                    maxSum = std::max(maxSum, maxSubArraySumNoLargerThanK(accs, k));
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
                    maxSum = std::max(maxSum, maxSubArraySumNoLargerThanK(accs, k));
                }            
            }
        }
        return maxSum;
    }
};
