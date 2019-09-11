/*
Search in Rotated Sorted Array II
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

*/
class Solution {
    public boolean search(int[] arr, int tag)
    {
        if (arr.length == 0)
        {
            return false;
        }

        int lt = 0; // left index
        int rt = arr.length - 1; // right index
        
        // Make sure left most != right most
        // This is the only difference of Search in Rotated Sorted Array II to Search in Rotated Sorted Array I
        while (rt > lt && arr[rt] == arr[lt])
        {
            rt--;
        }        
        int lastVal = arr[rt]; // last or right most value of arr
        
        // If target is bigger than last value, it is on left branch
        boolean targetIsOnLeft = (tag > lastVal);
        
        while (lt <= rt)
        {
            int mid = (lt + rt >> 1); // middle index
            int mv = arr[mid]; // middle value
            
            if (mv == tag)
            {
                return true;
            }
            
            // Whether middle value is on left or right
            boolean middleIsOnLeft = mv > lastVal;
            
            // If target and middle values are in same branch. compare mv and tag
            // If not in same branch, no need to compare mv and tag
            if (targetIsOnLeft && middleIsOnLeft && mv < tag ||
               !targetIsOnLeft && !middleIsOnLeft && mv < tag ||
               !targetIsOnLeft && middleIsOnLeft)
            {
                lt = mid + 1;
            }
            else
            {
                rt = mid - 1;
            }
        }
        return false;
    }
}
