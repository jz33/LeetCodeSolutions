/*
298. Binary Tree Longest Consecutive Sequence
https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

Example 2:

Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
*/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    private int maxLen = 0;
    
    public int longestConsecutive(TreeNode root) {
        if (root == null) {
            return 0;
        }
        maxLen = 0;
        preorder(root, root.val, 1);
        return maxLen;
    } 
    
    private void preorder(TreeNode node, int prev, int sofar) {
        if (node == null) {
            maxLen = Math.max(maxLen, sofar);
        } else if (node.val != prev + 1) {
            maxLen = Math.max(maxLen, sofar);
            preorder(node.left,  node.val, 1);
            preorder(node.right, node.val, 1);
        } else {
            preorder(node.left,  node.val, sofar + 1);
            preorder(node.right, node.val, sofar + 1);
        }
    }
}
