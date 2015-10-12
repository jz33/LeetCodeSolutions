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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if(root == null) return res;
        
        java.util.LinkedList<TreeNode> stack = new java.util.LinkedList<TreeNode>();
        TreeNode p = root;
        
        while(p != null || stack.size() > 0){
            if(p != null){
                stack.offerLast(p);
                p = p.left;
            } else {
                p = stack.pollLast();
                res.add(p.val);
                p = p.right;
            }
        }
        return res;
    }
}
