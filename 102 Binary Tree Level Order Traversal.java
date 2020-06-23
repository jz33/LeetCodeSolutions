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
    /**
    * Use array, avoiding using queue
    */
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        
        ArrayList<TreeNode> row = new ArrayList<>();
        row.add(root);
        while (!row.isEmpty()) {
            List<Integer> line = new ArrayList<>();
            ArrayList<TreeNode> nextRow = new ArrayList<>();
            for (TreeNode node : row) {
                line.add(node.val);
                if (node.left != null) {
                    nextRow.add(node.left);
                }
                if (node.right != null) {
                    nextRow.add(node.right);
                }
            }
            row = nextRow;
            result.add(line);
        }
        return result;
    }
}
