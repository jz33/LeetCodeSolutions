
/*
938. Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/

Given the root node of a binary search tree,
return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23

Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
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
    private int preorder(TreeNode node, int L, int R) {
        if (node == null) {
            return 0;
        }
        
        if (node.val < L) {
            return preorder(node.right, L, R);
        } else if (node.val > R) {
            return preorder(node.left, L, R);
        } else {
            return node.val + preorder(node.left, L, R) + preorder(node.right, L, R);
        }
    }

    public int rangeSumBST(TreeNode root, int L, int R) {
        return preorder(root, L, R);
    }
}
