/*
1214. Two Sum BSTs
https://leetcode.com/problems/two-sum-bsts/

Given two binary search trees, return True if and only if there is a node in the first tree and
a node in the second tree whose values sum up to a given integer target.

Example 1:

Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.

Example 2:



Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false
 

Constraints:

Each tree has at most 5000 nodes.
-10^9 <= target, node.val <= 10^9
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
public class BSTIterator {
    private TreeNode head;
    private Stack<TreeNode> parents = new Stack<>();
    private boolean ascending = true;

    public BSTIterator(TreeNode root, boolean ascending) {
        head = root;
        this.ascending = ascending;
    }
    
    /** @return the next smallest number */
    public int next() {
        while (head != null) {
            parents.push(head);
            head = ascending ? head.left : head.right;
        }
        
        TreeNode res = parents.pop();
        head = ascending ? res.right : res.left;
        return res.val;
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return head != null || !parents.isEmpty();
    }
}

class Solution {
    
    // Solution based on 173 Binary Search Tree Iterator
    public boolean twoSumBSTs(TreeNode root1, TreeNode root2, int target) {
        BSTIterator leftIterator = new BSTIterator(root1, true);
        BSTIterator rightIterator = new BSTIterator(root2, false);
        int leftVal = leftIterator.next();
        int rightVal = rightIterator.next();
        
        while (true) {
            int total = leftVal + rightVal;
            if (total == target) {
                return true;
            }
            if (total < target) {
                if (leftIterator.hasNext()) {
                    leftVal = leftIterator.next();
                } else {
                    return false;
                }
            } else {
                if (rightIterator.hasNext()) {
                    rightVal = rightIterator.next();
                } else {
                    return false;
                }
            }
        }
    }
}
