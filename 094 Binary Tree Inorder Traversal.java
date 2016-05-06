import java.util.*;
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public List<Integer> inorderTraversal(TreeNode root) {
    List<Integer> res = new ArrayList<Integer>();
    Stack<TreeNode> stack = new Stack<TreeNode>();
    TreeNode p = root;
    while(p != null || !stack.empty()){
        if(p != null){
            stack.push(p);
            p = p.left;
        } else {
            p = stack.pop();
            res.add(p.val);
            p = p.right;
        }
    }
    return res;
}
