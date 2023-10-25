/*
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

Constraints:

    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100
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
function maxDepth(root: TreeNode | null): number {
    let maxDepth = 0;
    let depth = 0;
    let curr: TreeNode | null = root;
    let last: TreeNode | null = null;
    const stack: TreeNode[] = [];
    while (curr || stack.length) {
        if (curr) {
            stack.push(curr);
            curr = curr.left;
            depth += 1;
        } else {
            const tail = stack[stack.length-1];
            if (tail.right && tail.right !== last) {
                curr = tail.right;
            } else {
                last = stack.pop();
                maxDepth = Math.max(maxDepth, depth)
                depth -= 1;
            }
        }
    }
    return maxDepth;
};
