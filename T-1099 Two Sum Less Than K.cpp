'''
1099. Two Sum Less Than K
https://leetcode.com/problems/two-sum-less-than-k/

Given an array A of integers and integer K, return the maximum S such that there exists
i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.

Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation: 
In this case it's not possible to get a pair sum less that 15.
'''
class Solution {
public:
    int twoSumLessThanK(vector<int>& A, int K) {
        std::stable_sort(A.begin(), A.end());
        size_t i = 0;
        size_t j = A.size() - 1;
        int res = -1;
        while (i < j) {
            int plus = A[i] + A[j];
            if (plus == K - 1) {
                return plus;
            } else if (plus < K ) {
                res = std::max(res, plus);
                i++;
            } else {
                j--;
            }
        }
        return res;
    }
};

