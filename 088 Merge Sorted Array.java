/*
88 Merge Sorted Array
https://oj.leetcode.com/problems/merge-sorted-array/
*/
public class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        
        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;
        
        for(;i > -1 && j > -1;k--){
            if(nums1[i] < nums2[j]){
                nums1[k] = nums2[j];
                j--;
            }
            else{
                nums1[k] = nums1[i];
                i--;
            }
        }
        
        for(;j > -1;j--){
            nums1[j] = nums2[j];
        }
    }
}
