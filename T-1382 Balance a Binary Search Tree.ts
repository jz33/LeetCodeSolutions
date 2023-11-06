/*
1382. Balance a Binary Search Tree
https://leetcode.com/problems/balance-a-binary-search-tree/

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

Example 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

Example 2:

Input: root = [2,1,3]
Output: [2,1,3]

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    1 <= Node.val <= 105

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

function inorderTraverse(root: TreeNode | null): number[] {
    if (!root) {
        return [];
    }
    const values: number[] = [];
    let curr: TreeNode | null = root;
    const stack: TreeNode[] = [];
    while (curr || stack.length) {
        if (curr) {
            stack.push(curr);
            curr = curr.left;
        } else {
            curr = stack.pop()!;
            values.push(curr.val);
            curr = curr.right;
        }
    }
    return values;
}

/**
 * Build a balanced tree. Same as 108. Convert Sorted Array to Binary Search Tree
 * @param left: left index, inclusive
 * @param right: right index, inclusive
 */
function inorderInit(
    values: number[],
    left: number,
    right: number
): TreeNode | null {
    if (left > right) {
        return null;
    }
    const mid = Math.floor((left + right) / 2);
    const newNode = new TreeNode(values[mid]);

    newNode.left = inorderInit(values, left, mid - 1);
    newNode.right = inorderInit(values, mid + 1, right);
    return newNode;
}

function balanceBST(root: TreeNode | null): TreeNode | null {
    const values = inorderTraverse(root);
    return inorderInit(values, 0, values.length - 1);
}
