'''
220. Contains Duplicate III
https://leetcode.com/problems/contains-duplicate-iii/

Given an array of integers, find out whether there are two distinct indices i and j in the array such that
the absolute difference between nums[i] and nums[j] is at most t and
the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
'''
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (k < 1 || t < 0) {
            return false;
        }
            
        TreeMap<Long, Integer> tm = new TreeMap<Long, Integer>(); // Counter {key : count}
        
        int size = nums.length;
        for (int i = 0; i < size; ++i) {
            Long n = new Long(nums[i]);
            
            // Remove out of bound key
            if (i - k > 0) {
                Long v = new Long(nums[i-k-1]);
                int c = tm.get(v);
                if (c == 1) {
                    tm.remove(v);
                } else {
                    tm.put(v, c - 1);
                }             
            }
            
            // Compare with closest value in map
            Long lo = tm.floorKey(n);
            if (lo != null && Math.abs(n - lo) <= t) {
                return true;           
            }
            Long hi = tm.ceilingKey(n);
            if (hi != null && Math.abs(n - hi) <= t) {
                return true;
            }
            
            // Put n
            tm.put(n, tm.getOrDefault(n, 0) + 1);
        }
        return false;
    }
}
