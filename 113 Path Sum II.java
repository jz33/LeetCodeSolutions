import java.util.*; 
/*
Path Sum II
https://leetcode.com/problems/path-sum-ii/
*/
public class Solution
{
    private int target = 0;
    private List<List<Integer>> pool = new Vector<List<Integer>>();
    
    class TreeNode
    {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }
    
    public void rec(TreeNode n, List<Integer> row, int sum)
    {
        if(n == null) return;
        sum += n.val;
        row.add(n.val);
        if(n.left == null && n.right == null)
        {
            if(sum == target)
            {
                pool.add(row);
            }
        }
        else if(n.left != null && n.right == null)
        {
            rec(n.left,row,sum);
        }
        else if(n.left != null && n.right == null)
        {
            rec(n.right,row,sum);
        }
        else
        {
            List<Integer> newRow = new Vector<Integer>();
            newRow.addAll(row);
            
            rec(n.left,row,sum);
            rec(n.right,newRow,sum);
        }
    }
        
    public List<List<Integer>> pathSum(TreeNode root, int target)
    {
        this.target = target;
        pool.clear();
        
        List<Integer> row = new Vector<Integer>();
        
        rec(root,row,0);
        return pool;
    }
}
