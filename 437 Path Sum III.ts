/*
437. Path Sum III
https://leetcode.com/problems/path-sum-iii/

Given the root of a binary tree and an integer targetSum,
return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards
(i.e., traveling only from parent nodes to child nodes).

Example 1:

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:

    The number of nodes in the tree is in the range [0, 1000].
    -109 <= Node.val <= 109
    -1000 <= targetSum <= 1000

*/

function pathSum(root: TreeNode | null, targetSum: number): number {
    let result = 0;
    // The sum from root to current node
    let rootPathSum: number = 0;
    // The counter of a path sum from root to a node
    const rootPathSumCounter = new Map<number, number>();
    let curr: TreeNode | null = root;
    let last: TreeNode | null = null;
    let stack: TreeNode[] = [];
    // Postorder
    while (curr || stack.length) {
        if (curr) {
            rootPathSum += curr.val;
            if (rootPathSum === targetSum) {
                // Increase result if the sum from root to current node is target sum
                result++;
            }
            // Increase result if the sum from a parent node to current node is target sum
            result += rootPathSumCounter.get(rootPathSum - targetSum) ?? 0;
            rootPathSumCounter.set(
                rootPathSum,
                (rootPathSumCounter.get(rootPathSum) ?? 0) + 1
            );
            stack.push(curr);
            curr = curr.left;
        } else {
            const tail = stack[stack.length - 1];
            if (tail.right && tail.right !== last) {
                curr = tail.right;
            } else {
                last = stack.pop()!;
                // As the last node is dropped, the root path sum needs to deduct this node,
                // as well as from the root path sum counter.
                rootPathSumCounter.set(
                    rootPathSum,
                    rootPathSumCounter.get(rootPathSum)! - 1
                );
                rootPathSum -= last.val;
            }
        }
    }
    return result;
}
