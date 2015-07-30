/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class BSTIterator
{
    public TreeNode visit;
    public java.util.Stack<TreeNode> nexts;
    
    public BSTIterator(TreeNode root)
    {
        visit = root;
        nexts = new java.util.Stack<TreeNode>();
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext()
    {
        return visit != null || !nexts.empty();
    }

    /** @return the next smallest number */
    public int next()
    {
        while(visit != null)
        {
            nexts.push(visit);
            visit = visit.left;
        }
        TreeNode curr = nexts.pop();
        visit = curr.right;
        return curr.val;
    }
}

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = new BSTIterator(root);
 * while (i.hasNext()) v[f()] = i.next();
 */
