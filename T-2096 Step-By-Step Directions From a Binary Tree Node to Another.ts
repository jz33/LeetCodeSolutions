/*
2096. Step-By-Step Directions From a Binary Tree Node to Another
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

You are given the root of a binary tree with n nodes.
Each node is uniquely assigned a value from 1 to n.
You are also given an integer startValue representing the value of the start node s,
and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t.
Generate step-by-step directions of such path as a string consisting of
only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

    'L' means to go from a node to its left child node.
    'R' means to go from a node to its right child node.
    'U' means to go from a node to its parent node.

Return the step-by-step directions of the shortest path from node s to node t.

Example 1:

Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.

Example 2:

Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.

Constraints:
    The number of nodes in the tree is n.
    2 <= n <= 105
    1 <= Node.val <= n
    All the values in the tree are unique.
    1 <= startValue, destValue <= n
    startValue != destValue
*/

/**
 * Find the target node, return the TARGET NODE TO ROOT PATH
 */
function getNodeAndRootPath(root: TreeNode, targetValue: number): TreeNode[] {
    const path: TreeNode[] = [];

    // Recursively iterate the tree, if find target value, update the path
    const postorder = (node: TreeNode | null): TreeNode | null => {
        if (!node) {
            return null;
        }
        if (node.val === targetValue) {
            path.push(node);
            return node;
        }
        const left = postorder(node.left);
        const right = postorder(node.right);
        if (!!left || !!right) {
            path.push(node);
            return node;
        }
        return null;
    };

    postorder(root);
    return path;
}

/**
 * Find the LCA of A & B based on node to root paths
 */
function getLca(pathA: TreeNode[], pathB: TreeNode[]): TreeNode {
    let ia = pathA.length - 1;
    let ib = pathB.length - 1;
    while (ia > -1 && ib > -1) {
        if (pathA[ia] !== pathB[ib]) {
            // The first time diverge. LCA is the previous node.
            return pathA[ia + 1];
        }
        ia--;
        ib--;
    }
    // If no diverge, 2 possible cases:
    // 1. A is child of B. LCA is B, pathA is longer;
    // 2. B is child of A. LCA is A, pathB is longer
    return ia > -1 ? pathB[0] : pathA[0];
}

function getDirections(
    root: TreeNode,
    startValue: number,
    destValue: number
): string {
    const startPath = getNodeAndRootPath(root, startValue);
    const destPath = getNodeAndRootPath(root, destValue);
    const lca = getLca(startPath, destPath);

    const startSteps: string[] = [];
    for (const node of startPath) {
        if (node === lca) {
            break;
        }
        startSteps.push('U');
    }
    
    const destSteps: string[] = [];
    for (let i = 0; i < destPath.length; i++) {
        const node = destPath[i];
        if (node === lca) {
            break;
        }
        const parent = destPath[i + 1];
        if (parent.left === node) {
            destSteps.push('L');
        } else {
            destSteps.push('R');
        }
    }
    return startSteps.concat(destSteps.reverse()).join('');
}
