/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    
    public int maxLen = 1;
    
    public void rec(TreeNode node, int prev, int acc){
        if(node == null){
            maxLen = Math.max(maxLen,acc);
        } else if(node.val != prev + 1){
            maxLen = Math.max(maxLen,acc);
            rec(node.left,  node.val, 1);
            rec(node.right, node.val, 1);
        } else {
            rec(node.left,  node.val, acc + 1);
            rec(node.right, node.val, acc + 1);
        }
    }
    
    public int longestConsecutive(TreeNode root) {
        if(root == null) return 0;
        maxLen = 1;
        rec(root.left,  root.val, 1);
        rec(root.right, root.val, 1);
        return maxLen;
    }
}
