/*
543. Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:

Input: root = [1,2]
Output: 1

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -100 <= Node.val <= 100
*/

function diameterOfBinaryTree(root: TreeNode | null): number {
    let maxNodeCount = 0;
    const postorder = (node: TreeNode | null): number => {
        if (!node) {
            return 0;
        }
        const leftDepth = postorder(node.left);
        const rightDepth = postorder(node.right);
        maxNodeCount = Math.max(maxNodeCount, leftDepth + rightDepth + 1);
        return Math.max(leftDepth, rightDepth) + 1;
    }
    postorder(root);
    return maxNodeCount - 1;
};
