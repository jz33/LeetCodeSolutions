#include <set>
#include <iterator>
using namespace std;
/*
480 Sliding Window Median
https://leetcode.com/problems/sliding-window-median
*/
class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        multiset<int> window(nums.begin(),nums.begin()+k);
        auto mid = next(window.begin(),(k-1) / 2);// oddy: center; even: center-1
        vector<double> res;
        res.push_back((k&1) ? double(*mid) : (double(*mid)+*next(mid))/2.0);
        for(auto i = k;i<nums.size();i++)
        {
            window.insert(nums[i]);
            if(nums[i] < *mid) // 
                mid--; // mid is still in center
            if(nums[i-k] <= *mid)
                mid++;
            window.erase(window.lower_bound(nums[i-k]));
            //cout<<*mid<<endl;
            res.push_back((k&1) ? double(*mid) : (double(*mid)+*next(mid))/2.0);
        }
        return res;
    }
};
