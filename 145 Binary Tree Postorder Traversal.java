import java.util.*;

public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
}
 
public List<Integer> postorderTraversal(TreeNode root) {
    List<Integer> res = new ArrayList<Integer>();
    if(root == null) return res;
    
    Stack<TreeNode> stack = new Stack<TreeNode>();
    stack.push(root);
    
    while(!stack.empty()){
        TreeNode p = stack.pop();
        res.add(p.val);
        if(p.left != null) stack.push(p.left);
        if(p.right != null) stack.push(p.right);
    }
    
    Collections.reverse(res);
    return res;
}
