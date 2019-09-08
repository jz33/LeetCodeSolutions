/*
Search in Rotated Sorted Array
https://oj.leetcode.com/problems/search-in-rotated-sorted-array/
*/
public class Solution {
    public int search(int[] arr, int tag)
    {
        if (arr.length == 0)
        {
            return -1;
        }

        int lt = 0; // left index
        int rt = arr.length - 1; // right index
        int lastVal = arr[rt]; // last or right most value of arr
        
        // If target is bigger than last value, it is on left branch
        boolean targetIsOnLeft = (tag > lastVal);
        
        while (lt <= rt)
        {
            int mid = (lt + rt >> 1); // middle index
            int mv = arr[mid]; // middle value
            
            if (mv == tag)
            {
                return mid;
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
        return -1;
    }
}
