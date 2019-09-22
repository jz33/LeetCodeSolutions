/*
153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1

Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

Example 3:
Input: [1,2,3]
Output: 1

Example 4:
Input: [0]
Output: 0
*/
class Solution
{
    public int findMin(int[] arr)
    {   
        int left = 0;
        int right = arr.length - 1;
        int lastVal = arr[right];
        
        while (left <= right)
        {         
            // Bottom cases
            if (left == right)
            {
                return arr[left];
            }
            if (left + 1 == right)
            {
                return Math.min(arr[left],arr[right]);
            }
            
            int mid = (left + right) >> 1;
            
            // mid - 1 is guaranteed inbound
            if (arr[mid-1] > arr[mid])
            {
                return arr[mid];
            }
            
            if (arr[mid] > lastVal)
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
        }
        return 0; // Not reachable
    }
}
