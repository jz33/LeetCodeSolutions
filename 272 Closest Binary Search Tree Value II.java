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
    public TreeNode getClosestNode(TreeNode root, double target) {
        TreeNode lt = null;
        TreeNode rt = null;
        while(root != null){
            if(target > root.val){
                lt = root;
                root = root.right;
            } else {
                rt = root;
                root = root.left;
            }
        }
        if(lt == null) return rt;
        if(rt == null) return lt;
        return target - lt.val <= rt.val - target ? lt : rt;
    }
    
    public TreeNode getPrev(TreeNode root, TreeNode curr){
        if(curr == null) return null;
        TreeNode prev = null;
        if(curr.left != null){
            prev = curr.left;
            while(prev.right != null){
                prev = prev.right;
            }
        } else {
            while(root.val != curr.val){
                if(root.val > curr.val){
                    root = root.left;
                } else if(root.val < curr.val){
                    prev = root;
                    root = root.right;
                }
            }
        }
        return prev;
    }
    
    public TreeNode getNext(TreeNode root, TreeNode curr){
        if(curr == null) return null;
        TreeNode next = null;
        if(curr.right != null){
            next = curr.right;
            while(next.left != null){
                next = next.left;
            }
        } else {
            while(root.val != curr.val){
                if(root.val > curr.val){
                    next = root;
                    root = root.left;
                } else if(root.val < curr.val){
                    root = root.right;
                }
            }
        }
        return next;
    }
    
    public List<Integer> closestKValues(TreeNode root, double target, int k) {
        List<Integer> res = new ArrayList<Integer>();
        if(root == null || k < 1) return res;
        TreeNode closest = getClosestNode(root,target);
        System.out.println(closest.val);
        res.add(closest.val);
        TreeNode prev = getPrev(root,closest);
        TreeNode next = getNext(root,closest);
        int i = 0;
        k--;
        for(;i < k && prev != null && next != null;i++){
            if(target - prev.val < next.val - target){
                res.add(prev.val);
                prev = getPrev(root,prev);
            } else {
                res.add(next.val);
                next = getNext(root,next);
            }
        }
        for(;i < k && prev != null;i++){
            res.add(prev.val);
            prev = getPrev(root,prev);
        }
        for(;i < k && next != null;i++){
            res.add(next.val);
            next = getNext(root,next);
        }
        return res;
    }
}
