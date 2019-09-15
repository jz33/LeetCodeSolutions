/*
173. Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/
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
public class BSTIterator
{
    // Solution is based on binary tree iterative in-order traverse
    // The head node for in-order traverse, i.e., the root of a new subtree (on the right)
    public TreeNode head;
    public java.util.Stack<TreeNode> visited;
    
    public BSTIterator(TreeNode root)
    {
        head = root;
        visited = new java.util.Stack<TreeNode>();
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext()
    {
        return head != null || !visited.empty();
    }

    /** @return the next smallest number */
    public int next()
    {
        // Move head to left most node
        while (head != null)
        {
            visited.push(head);
            head = head.left;
        }
        
        // The head is null now.
        // Get last visited node, which is the return node
        TreeNode lastVisited = visited.pop();
        
        // The head should point to the new subtree
        head = lastVisited.right;
        
        return lastVisited.val;
    }
}

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = new BSTIterator(root);
 * while (i.hasNext()) v[f()] = i.next();
 */
