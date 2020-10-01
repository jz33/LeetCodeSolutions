/*
257. Binary Tree Paths
https://leetcode.com/problems/binary-tree-paths/

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
*/

function binaryTreePaths(root: TreeNode | null): string[] {
    let pool: string[] = []

    function topdown(node: TreeNode, parents: number[]): void {
        if (node.left !== null && node.right !== null) {
            topdown(node.left, parents.concat([node.val]))
            topdown(node.right, parents.concat([node.val]))
        }
        else {
            parents.push(node.val)
            if (!node.left && !node.right) {
                pool.push(parents.join('->'))
            }
            else if (node.left !== null) {
                topdown(node.left, parents)
            }
            else if (node.right !== null) {
                topdown(node.right, parents)
            }
        }
    }

    if (root !== null) {
        topdown(root, [])
    }
    return pool
}
