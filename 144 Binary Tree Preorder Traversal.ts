/*
144 Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal
*/
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */
function preorderTraversal(root: TreeNode | null): number[] {
    const result: number[] = [];
    const stack: TreeNode[] = [];
    let curr = root;
    while (curr || stack.length > 0) {
        if (curr) {
            result.push(curr.val);
            stack.push(curr);
            curr = curr.left;
        } else {
            curr = stack.pop().right;
        }
    }
    return result;
};
