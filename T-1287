/*
1287. Element Appearing More Than 25% In Sorted Array
https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that
occurs more than 25% of the time.

Return that integer.

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
*/
class Solution {
    public int findSpecialInteger(int[] arr) {
        int cut = arr.length / 4;
        for (int i = 0; i + cut < arr.length; i++) {
            if (arr[i] == arr[i + cut]) {
                return arr[i];
            }
        }
        return -1;
    }
}
