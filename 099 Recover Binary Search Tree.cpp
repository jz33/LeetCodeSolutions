/*
99. Recover Binary Search Tree
https://leetcode.com/problems/recover-binary-search-tree/

Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
   
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
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
    public void recoverTree(TreeNode root) {
        Stack<TreeNode> stack = new Stack();
        TreeNode curr = root;
        TreeNode prev = null;
        TreeNode left = null;
        TreeNode right = null;
        
        while (curr != null || !stack.isEmpty()) {
            if (curr != null) {
                stack.push(curr);
                curr = curr.left;
            } else {
                curr = stack.pop();
                if (prev != null && prev.val > curr.val) {
                    // Meet a wrong pair
                    // Be careful of 2 cases:
                    // 1 2 3 5 4 6, L = 5, R = 4
                    // 1 2 5 4 3 6, L = 5, R = 3
                    if (left == null) {
                        left = prev;
                        right = curr;
                    } else {
                        right = curr;
                    }
                }
                prev = curr;
                curr = curr.right;
            }
        }
        
        if (left != null && right != null) {
            int val = left.val;
            left.val = right.val;
            right.val = val;
        }
    }
}
