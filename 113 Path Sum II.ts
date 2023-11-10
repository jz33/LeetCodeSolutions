/*
113 Path Sum II
https://leetcode.com/problems/path-sum-ii/

Given the root of a binary tree and an integer targetSum,
return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:

Input: root = [1,2], targetSum = 0
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000
*/
class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

type NodePath = {
    node: TreeNode;
    path: number[];
    total: number;
};

function pathSum(root: TreeNode | null, targetSum: number): number[][] {
    const result: number[][] = [];
    if (!root) {
        return result;
    }
    let row: NodePath[] = [{ node: root, path: [root.val], total: root.val }]; // [[current node, path values, sum]]

    while (row.length) {
        const newRow: NodePath[] = [];
        for (const { node, path, total } of row) {
            if (!node.left && !node.right) {
                if (total === targetSum) {
                    result.push(path);
                }
            }
            if (node.left) {
                newRow.push({
                    node: node.left,
                    path: path.concat([node.left.val]),
                    total: total + node.left.val,
                });
            }
            if (node.right) {
                newRow.push({
                    node: node.right,
                    path: path.concat([node.right.val]),
                    total: total + node.right.val,
                });
            }
        }
        row = newRow;
    }
    return result;
}
