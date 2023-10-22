/*
145. Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal
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

function postorderTraversal(root: TreeNode | null): number[] {
    const result: number[] = [];
    const stack: TreeNode[] = [];
    let curr: TreeNode | null = root;
    let last: TreeNode | null = null;
    while (curr || stack.length) {
        if (curr) {
            stack.push(curr);
            curr = curr.left;
        } else {
            const tail = stack[stack.length-1];
            if (tail.right && tail.right !== last) {
                curr = tail.right;
            } else {
                last = stack.pop();
                result.push(last.val);
            }
        }
    }
    return result;
};
