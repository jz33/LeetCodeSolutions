/*
333. Largest BST Subtree
https://leetcode.com/problems/largest-bst-subtree/

Given the root of a binary tree, find the largest subtree,
which is also a Binary Search Tree (BST),
where the largest means subtree has the largest number of nodes.

A Binary Search Tree (BST) is a tree in which all the nodes follow the below-mentioned properties:

    The left subtree values are less than the value of their parent (root) node's value.
    The right subtree values are greater than the value of their parent (root) node's value.

Note: A subtree must include all of its descendants.

Example 1:

Input: root = [10,5,15,1,8,null,7]
Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one. The return value is the subtree's size, which is 3.

Example 2:

Input: root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
Output: 2

Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -104 <= Node.val <= 104

Follow up: Can you figure out ways to solve it with O(n) time complexity?
*/

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

type CheckResult = {
    isBst: boolean;
    nodeCount: number;
    minVal: number;
    maxVal: number;
};

/**
 * Same idea as 1373. Maximum Sum BST in Binary Tree
 */
function largestBSTSubtree(root: TreeNode | null): number {
    let maxNodeCount = 0;

    const postorder = (node: TreeNode | null): CheckResult => {
        if (!node) {
            return {
                isBst: true,
                nodeCount: 0,
                // Want upper node check to be true,
                // notice how minVal and maxVal are set
                minVal: Number.MAX_SAFE_INTEGER,
                maxVal: Number.MIN_SAFE_INTEGER,
            };
        }
        const {
            isBst: isBstLeft,
            nodeCount: nodeCountLeft,
            minVal: minValLeft,
            maxVal: maxValLeft,
        } = postorder(node.left);

        const {
            isBst: isBstRight,
            nodeCount: nodeCountRight,
            minVal: minValRight,
            maxVal: maxValRight,
        } = postorder(node.right);

        const isBst =
            isBstLeft &&
            isBstRight &&
            node.val > maxValLeft &&
            node.val < minValRight;
        const nodeCount = nodeCountLeft + nodeCountRight + 1;
        if (isBst) {
            maxNodeCount = Math.max(maxNodeCount, nodeCount);
        }
        return {
            isBst,
            nodeCount,
            minVal: Math.min(minValLeft, node.val), // minValLeft can be MAX_SAFE_INTEGER
            maxVal: Math.max(maxValRight, node.val), // maxValRight can be MIN_SAFE_INTEGER
        };
    };

    postorder(root);
    return maxNodeCount;
}
