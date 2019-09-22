/*
154. Find Minimum in Rotated Sorted Array II
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
*/
class Solution
{
    public int findMin(int[] arr)
    {         
        int left = 0;
        int right = arr.length - 1;
        
        // Make sure left most != right most
        while (right > left && arr[right] == arr[left])
        {
            right--;
        }        
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
