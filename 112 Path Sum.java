/*
Path Sum
https://leetcode.com/problems/path-sum/
*/
public class Solution {
    
    class TreeNode
    {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }
 
    private int target = 0;
    private boolean flag = false;
    
    public void rec(TreeNode n, int buf)
    {
        if(n == null || flag == true) return;
        buf += n.val;
        if(buf == target && n.left == null && n.right == null)
        {
            flag = true;
            return;
        }
        rec(n.left, buf);
        rec(n.right,buf);
    }
    
    public boolean hasPathSum(TreeNode root, int sum)
    {
        target = sum;
        flag = false;
        rec(root,0);
        return flag;
    }
}
