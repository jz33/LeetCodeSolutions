/*
145. Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
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
    class VisitedNode {
        TreeNode node;
        boolean isRightChildVisited = false;

        VisitedNode(TreeNode node) {
            this.node = node;
            this.isRightChildVisited = false;
        }
    }
    
    public List<Integer> postorderTraversal(TreeNode root) {
        /*
        An iterative method without reverse
        */
        List<Integer> res = new ArrayList();
        Stack<VisitedNode> stack = new Stack();
        TreeNode p = root;
        while (p != null || !stack.isEmpty()) {
            if (p != null) {
                stack.add(new VisitedNode(p));
                p = p.left;
            } else if (stack.peek().isRightChildVisited) {
                p = stack.pop().node;
                res.add(p.val);
                p = null;
            } else {
                stack.peek().isRightChildVisited = true;
                p = stack.peek().node.right;
            }
        }
        return res;
    }
}
