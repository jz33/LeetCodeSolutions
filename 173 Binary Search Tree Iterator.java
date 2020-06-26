/*
173. Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.
*/
/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 *
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
class BSTIterator {
    private TreeNode head;
    private Stack<TreeNode> parents = new Stack<>();

    public BSTIterator(TreeNode root) {
        head = root;
    }
    
    /** @return the next smallest number */
    public int next() {
        while (head != null) {
            parents.push(head);
            head = head.left;
        }
        
        TreeNode res = parents.pop();
        head = res.right;
        return res.val;
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return head != null || !parents.isEmpty();
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
