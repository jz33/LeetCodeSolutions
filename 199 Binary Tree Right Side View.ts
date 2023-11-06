/*
199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/

Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:

Input: root = [1,null,3]
Output: [1,3]

Example 3:

Input: root = []
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 100].
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

function rightSideView(root: TreeNode | null): number[] {
    const result: number[] = [];
    if (!root) {
        return result;
    }
    // Even though only the right-most node's value on each level is needed,
    // it is necessary to save all nodes as it cannot guarantee right-most node
    // is always from the right-most parent.
    let row = [root];
    while (row.length) {
        const newRow: TreeNode[] = [];
        for (let nodeIndex = 0; nodeIndex < row.length; nodeIndex++) {
            const node = row[nodeIndex];
            if (nodeIndex === row.length - 1) {
                result.push(node.val);
            }
            if (node.left) {
                newRow.push(node.left);
            }
            if (node.right) {
                newRow.push(node.right);
            }
        }
        row = newRow;
    }
    return result;
};
