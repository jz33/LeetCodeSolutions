/*
704. Binary Search
https://leetcode.com/problems/binary-search/

Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
*/
class Solution {
    // Standard binary search method
    public int search(int[] nums, int target) {
        int lt = 0;
        int rt = nums.length - 1;
        
        while (lt <= rt) {
            int mid = (lt + rt >> 1);
            int midVal = nums[mid];
            
            if (midVal == target) {
                return mid;
            }
            
            if (midVal < target) {
                lt += 1;
            }
            else {
                rt -= 1;
            }
        }
        return -1;
    }
}
