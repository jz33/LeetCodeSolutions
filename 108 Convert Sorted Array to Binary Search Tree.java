/*
108. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which
the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
*/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length < 1) {
            return null;
        }
        
        return inorder(nums, 0, nums.length - 1);
    }
    
    /**
    * left and right: indexes of nums, inclusive
    */
    private TreeNode inorder(int[] nums, int left, int right) {
        if (left > right) {
            return null;
        }
        
        int mid = left + ((right - left) >> 1);
        TreeNode node = new TreeNode(nums[mid]);
        
        node.left = inorder(nums, left, mid - 1);
        node.right = inorder(nums, mid + 1, right);
        
        return node;
    }
}
