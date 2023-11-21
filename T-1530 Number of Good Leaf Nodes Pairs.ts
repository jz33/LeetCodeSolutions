/*
1530. Number of Good Leaf Nodes Pairs
https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

You are given the root of a binary tree and an integer distance.
A pair of two different leaf nodes of a binary tree is said to be good
if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

Example 1:

Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.

Example 2:

Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.

Example 3:

Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].

Constraints:
    The number of nodes in the tree is in the range [1, 210].
    1 <= Node.val <= 100
    1 <= distance <= 10
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
// Get count of pairs from 2 sorted arrays whose sum is less or equal to target
function getTwoArraySumCount(left: number[], right: number[], target: number): number {
    let count = 0;
    let ri = right.length - 1;
    let li = 0
    while (li < left.length && ri >= 0) {
        if (left[li] + right[ri] <= target) {
            // All (left[li], right[<=ri]) pais are valid
            count += ri + 1;
            li++;
        } else {
            ri--;
        }
    }
    return count;
}

function countPairs(root: TreeNode, distance: number): number {
    let result: number = 0;
    const postorder = (node: TreeNode): number[] => {
        let leafDepths = [];
        if (node.left && node.right) {
            const leftDists: number[] = postorder(node.left);
            const rightDists: number[] = postorder(node.right);
            result += getTwoArraySumCount(leftDists, rightDists, distance);
            leafDepths = leftDists.concat(rightDists).sort((a, b) => a - b);
        } else if (node.left) {
            leafDepths = postorder(node.left)
        } else if (node.right) {
            leafDepths = postorder(node.right);
        } else {
            leafDepths = [0];
        }
        return leafDepths.map(depth => depth + 1);
    }
    postorder(root);
    return result;
};
