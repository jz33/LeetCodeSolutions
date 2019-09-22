/*
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2

Explanation: the subarray [4,3] has the minimal length under the problem constraint.
    
*/
#include <algorithm>
class Solution
{
public:
    int minSubArrayLen(int s, vector<int>& nums)
    {
        int size = static_cast<int>(nums.size());
        int minLength = INT_MAX;
        int sum = 0; // current sum
        int i = 0; // to iterate nums
        int left = 0; // left index of current subarray
        while (i < size || sum >= s)
        {
            if (sum < s)
            {
                sum += nums[i];
                i++;
            }
            else
            {
                minLength = std::min(minLength, i - left);
                sum -= nums[left];
                left++;
            }
        }
        
        // Just for this question. If s never met, return 0
        return (minLength == INT_MAX) ? 0 : minLength;
    }
};
