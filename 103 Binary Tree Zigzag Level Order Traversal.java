/*
103 Binary Tree Zigzag Level Order Traversal
https://oj.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]
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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        
        // list is used like stack
        ArrayList<TreeNode> row = new ArrayList<>();
        row.add(root);
        
        // If true, add left child first then right child. If false, vice versa
        boolean leftToRight = true;
        
        while (!row.isEmpty()) {
            List<Integer> line = new ArrayList<>();
            ArrayList<TreeNode> nextRow = new ArrayList<>();
            
            // Iterate from back, like stack
            int size = row.size();
            for (int i = size - 1; i >= 0; --i) {
                TreeNode node = row.get(i);
                line.add(node.val);
                
                if (leftToRight) {
                    if (node.left != null) {
                        nextRow.add(node.left);
                    }
                    if (node.right != null) {
                        nextRow.add(node.right);
                    }
                } else {
                    if (node.right != null) {
                        nextRow.add(node.right);
                    }
                    if (node.left != null) {
                        nextRow.add(node.left);
                    }
                }
            }
            
            leftToRight = !leftToRight;
            row = nextRow;
            result.add(line);
        }
        return result;
    }
}
