/*
280. Wiggle Sort
https://leetcode.com/problems/wiggle-sort/
    
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
*/
#import <algorithm>
class Solution
{
public:
    void wiggleSort(vector<int>& nums)
    {
        if (nums.size() == 0)
        {
            return;    
        }
        
        bool oddy = true;
        for(int i = 0; i < nums.size()-1; i++)
        {
            if (oddy)
            {
                if(nums[i] > nums[i+1])
                {
                    std::swap(nums[i], nums[i+1]);
                }
            }
            else
            {
                if(nums[i] < nums[i+1])
                {
                    std::swap(nums[i], nums[i+1]);
                }
            }                        
            oddy = !oddy;
        }      
    }
};
