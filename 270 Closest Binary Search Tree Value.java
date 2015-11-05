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
    public int closestValue(TreeNode root, double target) {
        long lt = Long.MIN_VALUE;
        long rt = Long.MAX_VALUE;
        while(root != null){
            if(target > root.val){
                lt = root.val;
                root = root.right;
            } else {
                rt = root.val;
                root = root.left;
            }
        }
        return target - lt < rt - target ? (int)lt : (int)rt;
    }
}
