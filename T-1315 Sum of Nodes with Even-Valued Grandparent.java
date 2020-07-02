/*
1315. Sum of Nodes with Even-Valued Grandparent
https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

Given a binary tree, return the sum of values of nodes with even-valued grandparent.
(A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

Example 1:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18

Explanation: The red nodes are the nodes with even-value grandparent
while the blue nodes are the even-value grandparents.
 
Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
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
    private int result = 0;
    
    public void postorder(TreeNode node, int parentVal, int grandParentVal) {
        if (node == null) {
            return;
        }
        
        postorder(node.left, node.val, parentVal);
        postorder(node.right, node.val, parentVal);
        
        result += (1 - grandParentVal % 2) * node.val;
    }
    
    public int sumEvenGrandparent(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        result = 0;
        
        // Use 1 as grand parent value so 2nd level nodes are not count
        postorder(root.left, root.val, 1);
        postorder(root.right, root.val, 1);
        return result;
    }
}
